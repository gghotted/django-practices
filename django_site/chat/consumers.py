import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from chat.models import Room


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.romm_id = self.scope['url_route']['kwargs']['room_id']
        self.room_group_id = 'chat_%d' % self.romm_id

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_id,
            self.channel_name,
        )
        self.accept()
        try:
            room = Room.objects.get(id=self.romm_id)
            room.participant_num += 1
            room.save()
        except Room.DoesNotExist:
            Room.objects.create(id=self.romm_id, participant_num=1)

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_id,
            self.channel_name
        )
        room = Room.objects.get(id=self.romm_id)
        room.participant_num -= 1
        room.save()
        

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_id,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    def chat_message(self, event):
        message = event['message']
        self.send(text_data=json.dumps({
            'message': message
        }))


class LobbyConsumer(WebsocketConsumer):
    def connect(self):
        self.group_id = 'lobby'
        async_to_sync(self.channel_layer.group_add)(
            self.group_id,
            self.channel_name,
        )
        self.accept()
    
    def disconnect(self, code):
        pass

    def lobby_message(self, event):
        message = event['message']
        self.send(text_data=json.dumps({
            'message': message
        }))
