import json
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *
import channels.layers
from asgiref.sync import async_to_sync


def send_message(event):
    message = event['text']
    channel_layer = channels.layers.get_channel_layer()
    # Send message to WebSocket
    async_to_sync(channel_layer.send)(text_data=json.dumps(
        message
    ))


@receiver(post_save, sender=Log, dispatch_uid='update_status')
def update_status(sender, instance, **kwargs):
    room_name = scope['url_route']['kwargs']['room_name']
    room_group_name = 'chat_%s' % room_name

    message = {
        'topic': instance.topic,
        'created': instance.created,
    }

    channel_layer = channels.layers.get_channel_layer()

    async_to_sync(channel_layer.group_send)(
        room_group_name,
        {
            'type': 'send_message',
            'text': message
        }
    )
