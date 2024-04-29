from django import forms
from django.db.models import Q
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
            Q(username__istartswith=self.cleaned_data['search']) |
            Q(first_name__istartswith=self.cleaned_data['search']) |
            Q(last_name__istartswith=self.cleaned_data['search'])
        ).exclude(
            username=self.cleaned_data['user'].username
        )
