from django import forms
from rest_framework.exceptions import ValidationError
from service_objects.services import Service

from models_app.models import User


class UserCheckUsernameService(Service):
    username = forms.CharField()

    def process(self):
        self.check_username()

    def check_username(self):
        username = User.objects.filter(username=self.cleaned_data['username'])
        if username.exists():
            raise ValidationError('Username is already exists')
