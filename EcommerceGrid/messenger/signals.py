from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *
import channels.layers
from asgiref.sync import async_to_sync


@receiver(post_save, sender=Message, dispatch_uid='conversations')
def conversations(sender, instance, **kwargs):
    room_name = instance.conversation.name
    room_group_name = 'conversation_%s' % room_name

    message = {
        'user': instance.user.username,
        'message': instance.msg,
        # 'attachment': instance.attachment,
        'timestamp': str(instance.timestamp),
    }

    channel_layer = channels.layers.get_channel_layer()

    async_to_sync(channel_layer.group_send)(
        room_group_name,
        {
            'type': 'send_conversation',
            'message': message
        }
    )
