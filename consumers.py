from channels.generic.websocket import AsyncWebsocketConsumer
import json


class CommentConsumer(AsyncWebsocketConsumer):
    """
    This class consists of a basic consumer that
    accepts WebSocket connection
    """

    async def connect(self):
        """
        :connect
        """

        await self.channel_layer.group_add(
            "comments",
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        """
        :disconnect
        """

        await self.channel_layer.group_discard(
            "comments",
            self.channel_name
        )

    async def receive(self, text_data):
        """
        :receive
        """

        text_data_json = json.loads(text_data)
        comments = text_data_json['comments']
        await self.channel_layer.group_send(
            "comments",
            {
            'type': 'Comments',
            'comments': comments,
            }
        )

    async def Comments(self, event):
        comments = event['comments']
        await self.send(text_data=json.dumps({
            'comments': comments,
        }))
