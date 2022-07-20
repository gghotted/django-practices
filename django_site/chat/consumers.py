import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.contrib.auth.models import AnonymousUser
from django_site.middleware import get_validated_token


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.user = self.scope['user']
        if isinstance(self.user, AnonymousUser):
            return

        self.romm_id = self.scope['url_route']['kwargs']['room_id']
        self.room_group_id = 'chat_%d' % self.romm_id
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_id,
            self.channel_name,
        )
        self.accept()

    def disconnect(self, code):
        if hasattr(self, 'room_group_id'):
            async_to_sync(self.channel_layer.group_discard)(
                self.room_group_id,
                self.channel_name
            )

    def receive(self, text_data=None, bytes_data=None):
        if get_validated_token(self.scope['raw_token']) is None:
            self.disconnect(None)
            return

        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_id,
            {
                'type': 'chat_message',
                'message': f'{self.user.username}: {message}'
            }
        )

    def chat_message(self, event):
        if get_validated_token(self.scope['raw_token']) is None:
            self.disconnect(None)
            return

        message = event['message']
        self.send(text_data=json.dumps({
            'message': message
        }))
