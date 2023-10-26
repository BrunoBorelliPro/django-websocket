import json
from django.shortcuts import render
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


# Create your views here.
def index(request):
    return render(request, "index.html")


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        print(f"Conectando com o Websocket")
        self.room_group_name = "test"

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )
        return super().accept()

    def disconnect(self, code):
        print(f"Desconectando do Websocket")

        pass

    def receive(self, text_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json.get("message")
        print(f"message: {message}")

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "chat_message", "message": message}
        )

    def chat_message(self, event):
        message = event["message"]
        self.send(text_data=json.dumps({"type": "chat", "message": message}))
