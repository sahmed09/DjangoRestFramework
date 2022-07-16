import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import *
from urllib.parse import parse_qs
from django.db import close_old_connections
from rest_framework_simplejwt.tokens import UntypedToken
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from jwt import decode as jwt_decode
from django.conf import settings
from django.contrib.auth.models import User
from asgiref.sync import sync_to_async


@sync_to_async
def get_user(user_id):
    return User.objects.filter(id=user_id).first()


@sync_to_async
def get_permission(user, conversation):
    return ConversationMember.objects.filter(user=user, conversation__name=conversation).exists()


class MessageConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        close_old_connections()

        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'conversation_%s' % self.room_name

        token = parse_qs(self.scope["query_string"].decode("utf8"))["token"][0]

        try:
            UntypedToken(token)
        except (InvalidToken, TokenError) as e:  # Token is invalid
            print(e)
            return None
        else:
            decoded_data = jwt_decode(token, settings.SECRET_KEY, algorithms=["HS256"])

            user = await get_user(decoded_data["user_id"])
            role = await get_permission(user, self.room_name)
            # print(user, role)

            if role:
                # Join room group
                await self.channel_layer.group_add(
                    self.room_group_name,
                    self.channel_name
                )

                await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from room group
    async def send_conversation(self, event):
        message = event['message']
        print(message)

        await self.send(text_data=json.dumps(
            message
        ))
