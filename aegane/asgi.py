import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aegane.settings')  # Replace 'myproject' with your project name
django.setup()

from django.core.asgi import get_asgi_application
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
        "http": get_asgi_application(),
        "websocket": AuthMiddlewareStack(
            URLRouter(
               websocket_urlpatterns
            )
        ),
    }
)

