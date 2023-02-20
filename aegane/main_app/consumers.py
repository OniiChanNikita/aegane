import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import MessageChat


class ChatRoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.chat_box_name = self.scope["url_route"]["kwargs"]["slug_num"]
        self.group_name = "chat_%s" % self.chat_box_name
        # self.user = , self.user1
        # if MessageChat.objects.get()
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    # This function receive messages from WebSocket.
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        username = text_data_json["username"]
        # await MessageChat.objects.create
        await self.channel_layer.group_send(
            self.group_name,
            {
                "type": "chatbox_message",
                "message": message,
                "username": username,
            },
        )

    # Receive message from room group.
    async def chatbox_message(self, event):
        message = event["message"]
        username = event["username"]
        await self.send(
            text_data=json.dumps(
                {
                    "message": message,
                    "username": username,
                }
            )
        )

    pass
