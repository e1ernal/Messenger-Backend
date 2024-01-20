from django import forms
from service_objects.services import Service

from models_app.models import User


class UserSearchService(Service):
    search = forms.CharField()

    def process(self):
        return self.get_users

    @property
    def get_users(self):
        return User.objects.filter(
            username__istartswith=self.cleaned_data['search']
        )
