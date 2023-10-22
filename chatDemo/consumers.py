import json
import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer


class DatabaseChangesConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

        # Start a periodic task to send messages every 5 seconds
        self.periodic_task = asyncio.ensure_future(self.send_messages_periodically())

    async def disconnect(self, close_code):
        # Cancel the periodic task when the connection is closed
        if hasattr(self, 'periodic_task'):
            self.periodic_task.cancel()

    async def receive(self, text_data):
        message = json.loads(text_data)
        await self.send(text_data=json.dumps({
            'message': message
        }))

    async def send_messages_periodically(self):
        while True:
            # Send a message to the connected clients
            await self.send_message("This is a message sent every 5 seconds.")
            await asyncio.sleep(5)  # Wait for 5 seconds before sending the next message

    async def send_message(self, message):
        await self.send(text_data=json.dumps({
            'message': message
        }))
