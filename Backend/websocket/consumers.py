import json

from channels.generic.websocket import AsyncWebsocketConsumer


class WsTestConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.chat_name = "direct_chat_" + str(self.scope['url_route']['kwargs']['pk'])
        await self.channel_layer.group_add(
            self.chat_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.chat_name,
            self.channel_name
        )

    async def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        await self.channel_layer.group_send(
            self.chat_name,
            data
        )

    async def message(self, event):
        await self.send(text_data=json.dumps({
            **event
        }))
