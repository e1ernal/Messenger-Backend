from django import forms
from rest_framework.exceptions import ValidationError
from service_objects.fields import ModelField
from service_objects.services import Service

from models_app.models import User


class UserUpdateService(Service):
    user = ModelField(User)
    username = forms.CharField(required=False)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)

    def process(self):
        return self.update_user()

    def update_user(self):
        user = self.cleaned_data["user"]
        if self.cleaned_data["username"]:
            if self.check_username():
                raise ValidationError('Username already exists')
            user.username = self.cleaned_data["username"]
        if self.cleaned_data["first_name"]:
            user.first_name = self.cleaned_data["first_name"]
        if self.cleaned_data["last_name"]:
            user.last_name = self.cleaned_data["last_name"]
        user.save()
        return user

    def check_username(self):
        return User.objects.filter(
            username=self.cleaned_data["username"]
        ).exists()
