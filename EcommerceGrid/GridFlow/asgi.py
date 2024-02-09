"""
ASGI config for GridFlow project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from django.urls import path
from shop.consumers import ShopConsumer
from messenger.consumers import MessageConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GridFlow.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path('ws/shop/<room_name>/', ShopConsumer.as_asgi()),
            path('ws/messenger/<room_name>/', MessageConsumer.as_asgi()),
        ])
    ),
})
