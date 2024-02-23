from django import forms
from service_objects.fields import ModelField
from service_objects.services import Service

from models_app.models import User


class UserSearchService(Service):
    search = forms.CharField()
    user = ModelField(User)

    def process(self):
        return self.get_users

    @property
    def get_users(self):
        return User.objects.filter(
            username__istartswith=self.cleaned_data['search']
        ).exclude(
            username=self.cleaned_data['user'].username
        )
