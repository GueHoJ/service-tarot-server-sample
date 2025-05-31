def get_gpt_parameters(user_id=None, session_id=None):
    from .domain.CONAI_CHATBOT_GPT_PARAMETERS_MST import ConaiChatbotGptParametersMst
    """
    Retrieve GPT parameters dynamically based on user or session ID.
    """
    try:
        if not user_id:
            return "User ID is required to retrieve GPT parameters."
        if not session_id:
            return "Session ID is required to retrieve GPT parameters."
        if user_id and session_id:
            params = ConaiChatbotGptParametersMst.objects.get(user_id=user_id, session_id=session_id)
            # Convert model instance to dictionary with snake_case keys
            return {
                "conai_chatbot_gpt_parameters_mst_id": params.conai_chatbot_gpt_parameters_mst_id,
                "user_id": params.user_id,
                "session_id": params.session_id,
                "config_name": params.config_name,
                "model": params.model,
                "temperature": params.temperature,
                "max_tokens": params.max_tokens,
                "stop_sequences": params.stop_sequences,
                "top_p": params.top_p,
                "frequency_penalty": params.frequency_penalty,
                "presence_penalty": params.presence_penalty,
                "description": params.description,
                "created_at": params.created_at,
                "updated_at": params.updated_at,
            }
    except ConaiChatbotGptParametersMst.DoesNotExist:
        # Return default parameters if none are found
        return {
            "model": "gpt-3.5-turbo",
            "temperature": 0.7,
            "max_tokens": 1024,
            "stop_sequences": [],
            "top_p": 1.0,
            "frequency_penalty": 0.0,
            "presence_penalty": 0.0,
        }


def store_message(message, user_id=None, session_id=None):
    """
    Store a message in the database.
    """
    from chatbot.containers import registry
    from chatbot.application.service.chatbot_conai_chatbot_message_mst_restful_service import \
        ChatbotConaiChatbotMessageMstRestfulService

    # Create a container from the registry
    container = registry.create_container()

    print(f"container ==> {container}")
    # Resolve MyService from the container
    service = container.get(ChatbotConaiChatbotMessageMstRestfulService)

    post_params = {
        "conversationId": session_id,
        "userId": user_id,
        "role": message['role'],
        "message": message['content'],
    }

    if message.get("mediaType"):
        post_params["mediaType"] = message["mediaType"]

    if message.get("mediaUrl"):
        post_params["mediaUrl"] = message["mediaUrl"]

    print(f"store_message : message ==> {message}")
    serializer = service.chatbot_conai_chatbot_message_mst_post(post_params)
    print(f"store_message : serializer.is_valid() ==> {serializer.is_valid()}")
    # if serializer.is_valid(raise_exception=True):

    if serializer.is_valid():
        serializer.save()
        return "Message stored successfully."
    else:
        return serializer.errors


def update_message(message, user_id=None, session_id=None):
    """
    Update a message in the database.
    """
    from chatbot.containers import registry
    from chatbot.application.service.chatbot_conai_chatbot_message_mst_restful_service import \
        ChatbotConaiChatbotMessageMstRestfulService
    from app.utils.common_utils import log_info

    # Create a container from the registry
    container = registry.create_container()

    log_info(f"container ==> {container}")
    # Resolve MyService from the container
    service = container.get(ChatbotConaiChatbotMessageMstRestfulService)

    get_params = {
        "conversationId": session_id,
        "userId": user_id,
        "role": "system",
    }

    log_info("\n=== Update Message Debug Information ===")
    log_info(f"Input Parameters:")
    log_info(f"- message: {message}")
    log_info(f"- user_id: {user_id}")
    log_info(f"- session_id: {session_id}")
    log_info(f"- get_params: {get_params}")

    get_serializer = service.chatbot_conai_chatbot_message_mst_get(get_params)
    
    # Check if there are any records
    if not get_serializer.data:
        log_info("No messages found in the serializer")
        store_message(message, user_id, session_id)
    else:
        log_info(f"Found {len(get_serializer.data)} messages")
        # Get the first message's ID
        message_id = get_serializer.data[0]['conaiChatbotMessageMstId']
        log_info(f"Found message ID: {message_id}")
        
        # Now you can use this message_id for updates
        put_params = {
            "conaiChatbotMessageMstId": message_id,
            "message": message['content'],
            # Add other fields you want to update
        }
        if get_serializer.data[0].get("message") == message['content']:
            log_info("Message content is the same. No need to update.")
            return "Message content is the same. No need to update."

        put_result = service.chatbot_conai_chatbot_message_mst_put(put_params)
        log_info(f"put_result ==> {put_result}")
        put_serializer = put_result.get("result_serializer")
        log_info(f"put_serializer.is_valid() ==> {put_serializer.is_valid()}")
        if put_serializer.is_valid():
            put_serializer.save()
            return "Message updated successfully."
        else:
            return put_serializer.errors


def update_conversation_history(history_message, user_id=None, session_id=None):
    """
    Update a message in the database.
    """
    from chatbot.containers import registry
    from chatbot.application.service.chatbot_conai_chatbot_conversation_history_mst_restful_service import \
        ChatbotConaiChatbotConversationHistoryMstRestfulService
    from app.utils.common_utils import log_info

    # Create a container from the registry
    container = registry.create_container()

    log_info(f"container ==> {container}")
    # Resolve MyService from the container
    service = container.get(ChatbotConaiChatbotConversationHistoryMstRestfulService)

    get_params = {
        "conversationId": session_id,
        "userId": user_id,
    }

    log_info("\n=== Update Conversation History Debug Information ===")
    log_info(f"Input Parameters:")
    log_info(f"- message: {history_message}")
    log_info(f"- user_id: {user_id}")
    log_info(f"- session_id: {session_id}")
    log_info(f"- get_params: {get_params}")

    get_serializer = service.chatbot_conai_chatbot_conversation_history_mst_get(get_params)

    # Check if there are any records
    if not get_serializer.data:
        log_info("No messages found in the serializer")
        post_params = get_params
        post_params["historyData"] = history_message
        post_serializer = service.chatbot_conai_chatbot_conversation_history_mst_post(post_params, user_id, session_id)
        if post_serializer.is_valid():
            post_serializer.save()
            print("Conversation history stored successfully.")
            return "Conversation history stored successfully."
        else:
            print(post_serializer.errors)
            return post_serializer.errors
    else:
        log_info(f"Found {len(get_serializer.data)} messages")
        # Get the first message's ID
        message_id = get_serializer.data[0]['conaiChatbotConversationHistoryMstId']
        log_info(f"Found message ID: {message_id}")

        # Now you can use this message_id for updates
        put_params = {
            "conaiChatbotConversationHistoryMstId": message_id,
            "historyData": history_message,
            # Add other fields you want to update
        }
        if get_serializer.data[0].get("historyData") == history_message:
            log_info("Message content is the same. No need to update.")
            return "Message content is the same. No need to update."

        put_result = service.chatbot_conai_chatbot_conversation_history_mst_put(put_params)
        log_info(f"put_result ==> {put_result}")
        put_serializer = put_result.get("result_serializer")
        log_info(f"put_serializer.is_valid() ==> {put_serializer.is_valid()}")
        if put_serializer.is_valid():
            put_serializer.save()
            print("Conversation history updated successfully.")
            return "Message updated successfully."
        else:
            print(put_serializer.errors)
            return put_serializer.errors