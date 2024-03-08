from functools import lru_cache

from django import forms
from rest_framework.exceptions import ValidationError
from service_objects.fields import ModelField
from service_objects.services import Service

from models_app.models import User, DirectChat, Message


class MessageListService(Service):
    user = ModelField(User)
    direct_id = forms.IntegerField()

    def process(self):
        self.check_permission()
        return self._messages

    @property
    def _messages(self):
        return Message.objects.filter(direct=self._direct_chat)

    def check_permission(self):
        direct = self._direct_chat
        if direct.first_user != self.cleaned_data['user'] and direct.second_user != self.cleaned_data['user']:
            raise ValidationError("Permission denied")

    @property
    @lru_cache()
    def _direct_chat(self):
        directs = DirectChat.objects.filter(id=self.cleaned_data['direct_id'])
        if not directs.exists():
            raise ValidationError("Direct chat not found")
        return directs.first()
