"""
ASGI config for django_websocket project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from django.urls import re_path

from channels.routing import ProtocolTypeRouter, URLRouter

from core.views import ChatConsumer

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_websocket.settings")


websocket_urlpatterns = [
    re_path("chat/ws", ChatConsumer.as_asgi()),
]

application = get_asgi_application()

application = ProtocolTypeRouter(
    {"http": get_asgi_application(), "websocket": URLRouter(websocket_urlpatterns)}
)
