from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db.models.signals import post_save
from django.dispatch import receiver

from chat.models import Room


@receiver(post_save, sender=Room)
def room_post_save(sender, **kwargs):
    layer = get_channel_layer()
    async_to_sync(layer.group_send)(
        'lobby',
        {
            'type': 'lobby_message',
            'message': list(Room.objects.values())
        }
    )
