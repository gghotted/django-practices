from django.urls import path

from chat.consumers import ChatConsumer, LobbyConsumer

websocket_urlpatterns = [
    path('ws/chat/<int:room_id>/', ChatConsumer.as_asgi()),
    path('ws/chat/lobby/', LobbyConsumer.as_asgi()),
]
