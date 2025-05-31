import logging
from channels.generic.websocket import AsyncWebsocketConsumer
import json
from asgiref.sync import sync_to_async
from channels.db import database_sync_to_async
from channels.exceptions import DenyConnection
from jwt import decode
from django.conf import settings

from app.utils.common_utils import log_info
from chatbot.chatbot_openai import chat_with_gpt_params_stream

logger = logging.getLogger(__name__)


class ChatConsumer(AsyncWebsocketConsumer):
    active_connections = set()

    async def connect(self):
        try:
            # Get the token from the URL query parameters
            query_string = self.scope.get('query_string', b'').decode()
            logger.info(f"Received query string: {query_string}")
            
            token = None
            if query_string:
                try:
                    token_part = query_string.split('token=', 1)[1]
                    token = token_part.split('?')[0]
                    logger.info(f"Successfully extracted token from query string")
                except IndexError:
                    token = None
                    logger.warning("Failed to extract token from query string")

            if not token:
                # Check for token in headers
                headers = dict(self.scope['headers'])
                auth_header = headers.get(b'authorization', b'').decode()
                token = auth_header.replace('Bearer ', '') if auth_header else ''
                logger.info("Using token from authorization header")

            if not token:
                logger.error("No token provided in query params or headers")
                await self.close(code=4001)
                return

            # Verify it's a valid JWT format before trying to decode
            token_parts = token.split('.')
            if len(token_parts) != 3:
                logger.error(f"Invalid JWT format. Token parts: {len(token_parts)}")
                await self.close(code=4002)
                return

            # Verify the JWT token
            try:
                payload = decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            except Exception as e:
                logger.error(f"Token validation failed: {str(e)}")
                await self.close(code=4002)
                return

            user = await self.get_user(payload['user_id'])
            
            if not user:
                logger.error(f"User not found for ID: {payload['user_id']}")
                await self.close(code=4003)
                return

            self.scope['user'] = user
            logger.info(f"WebSocket connection established for user id: {user.id}, username: {user.username}")
            
            # Add to active connections before accepting
            self.active_connections.add(self)
            await self.accept()
            logger.info("WebSocket connection accepted successfully")

        except Exception as e:
            logger.error(f"WebSocket connection failed: {str(e)}", exc_info=True)
            await self.close(code=4002)

    @database_sync_to_async
    def get_user(self, user_id):
        # Import User model here instead of at module level
        from django.contrib.auth import get_user_model
        User = get_user_model()
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None

    async def disconnect(self, close_code):
        logger.info(f"WebSocket disconnected with close code {close_code}")
        try:
            self.active_connections.remove(self)
        except KeyError:
            pass

    async def receive(self, text_data):
        try:
            data = json.loads(text_data) if isinstance(text_data, str) else {}
            chatbot_params = data.get("chatbotParams", {})
            user_id = data.get("userId", {})
            session_id = data.get("sessionId", {})
            log_info(f"Received data : {data}\n"
                     f"chatbotParams: {chatbot_params}")

            if not chatbot_params:
                await self.send(json.dumps({"error": "chatbotParams is empty or missing."}))
                return

            if not user_id:
                await self.send(json.dumps({"error": "userId is empty or missing."}))
                return

            if not session_id:
                await self.send(json.dumps({"error": "sessionId is empty or missing."}))
                return

            async for chunk in chat_with_gpt_params_stream(chatbot_params, user_id=user_id, session_id=session_id):
                if isinstance(chunk, str):
                    if chunk.startswith('{"type":"messages_update"'):
                        # Store updated messages in the session if needed
                        messages_data = json.loads(chunk)
                        await self.send(json.dumps(messages_data))
                    elif chunk.startswith('{"type":"message_end"'):
                        # Handle end of message signal
                        await self.send(chunk)
                    else:
                        await self.send(chunk)
                else:
                    await self.send(chunk)

        except json.JSONDecodeError as e:
            await self.send(json.dumps({"error": f"Invalid JSON format: {str(e)}"}))
        except Exception as e:
            await self.send(json.dumps({"error": f"Unexpected error: {str(e)}"}))
