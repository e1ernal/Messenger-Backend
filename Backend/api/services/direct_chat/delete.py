from django import forms
from rest_framework.exceptions import ValidationError
from service_objects.fields import ModelField
from service_objects.services import Service

from models_app.models import DirectChat, User


class DirectChatDeleteService(Service):
    id = forms.IntegerField()
    user = ModelField(User)

    def process(self):
        self.direct_chat = self.check_direct_chat_presence()
        self.direct_chat_delete()

    def check_direct_chat_presence(self):
        direct_chat = DirectChat.objects.filter(id=self.cleaned_data['id'])
        if not direct_chat.exists():
            raise ValidationError('Direct chat with this id not found', code=404)
        direct_chat = direct_chat.first()
        if self.cleaned_data['user'] != direct_chat.first_user and self.cleaned_data['user'] != direct_chat.second_user:
            raise ValidationError('Your user is not a member of this chat', code=400)
        return direct_chat

    def direct_chat_delete(self):
        self.direct_chat.delete()
