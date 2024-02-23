from django import forms
from service_objects.fields import ModelField
from service_objects.services import Service
from models_app.models import User


class UserDeleteService(Service):
    user = ModelField(User)

    def process(self):
        return self.delete_user

    @property
    def delete_user(self):
        user = self.cleaned_data['user']
        user.delete()
