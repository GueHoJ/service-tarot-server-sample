from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import re_path
from chatbot.adapter._in.chat_consumer import ChatConsumer

websocket_urlpatterns = [
    re_path(r'ws/chat/$', ChatConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    'websocket': URLRouter(websocket_urlpatterns)
})