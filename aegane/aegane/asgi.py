from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import re_path
from main_app import consumers

# URLs that handle the WebSocket connection are placed here.
websocket_urlpatterns=[
                    re_path(
                        r"chat/(?P<slug_num>\d+)/$", consumers.ChatRoomConsumer.as_asgi()
                    ),
                ]

application = ProtocolTypeRouter(
    {
        "websocket": AuthMiddlewareStack(
            URLRouter(
               websocket_urlpatterns
            )
        ),
    }
)