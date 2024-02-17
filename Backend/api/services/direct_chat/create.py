from django import forms
from django.db.models import Q
from rest_framework.exceptions import ValidationError
from service_objects.fields import ModelField
from service_objects.services import Service

from models_app.models import User, DirectChat


class DirectChatCreateService(Service):
    first_user = ModelField(User)
    second_user = forms.IntegerField()

    def process(self):
        self.second_user = self.check_user_presence()
        self.check_chat_exists()
        return self.direct_chat_create()

    def check_user_presence(self):
        user = User.objects.filter(id=self.cleaned_data['second_user'])
        if not user.exists():
            raise ValidationError('User with this id not found', code=404)
        if user.first() == self.cleaned_data['first_user']:
            raise ValidationError('You cant create direct chat with your self', code=400)
        return user.first()

    def check_chat_exists(self):
        direct_chat = DirectChat.objects.filter(
            Q(first_user=self.cleaned_data['first_user'],
              second_user=self.second_user) |
            Q(first_user=self.second_user,
              second_user=self.cleaned_data['first_user'])
        )
        if direct_chat.exists():
            raise ValidationError('Direct chat for users already exists', code=400)

    def direct_chat_create(self):
        return DirectChat.objects.create(
            first_user=self.cleaned_data['first_user'],
            second_user=self.second_user
        )
