from django import forms
from rest_framework.exceptions import ValidationError
from service_objects.fields import ModelField
from service_objects.services import Service

from models_app.models import User, DirectChat, Message


class MessageCreateService(Service):
    author = ModelField(User)
    direct = forms.IntegerField()
    text = forms.CharField()

    def process(self):
        return self.create_message()

    def create_message(self):
        direct_chat = DirectChat.objects.filter(id=self.cleaned_data['direct'])
        if not direct_chat.exists():
            raise ValidationError("Chat not found")

        message = Message.objects.create(
            author=self.cleaned_data['author'],
            direct=self.cleaned_data['direct'],
            text=self.cleaned_data['text']
        )
        return message
