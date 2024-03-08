from django.urls import path
from websocket.consumers import *

websocket_patterns = [
    path('ws/direct_chat/<str:pk>/', WsTestConsumer.as_asgi())
]
