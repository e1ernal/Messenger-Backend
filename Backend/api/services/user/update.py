import base64
from datetime import datetime

from django import forms
from django.core.files.base import ContentFile
from rest_framework.exceptions import ValidationError
from service_objects.fields import ModelField
from service_objects.services import Service

from models_app.models import User


class UserUpdateService(Service):
    user = ModelField(User)
    username = forms.CharField(required=False)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    image = forms.CharField(required=False)

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
        if self.cleaned_data["image"]:
            user.image = self.convert_base64_to_image(self.cleaned_data["image"])
        user.save()
        return user

    @staticmethod
    def convert_base64_to_image(image):
        try:
            type_image, image = image.split(';base64,')
            name = datetime.now().strftime("%Y%m%d%H%M%S")
            return ContentFile(
                base64.b64decode(image),
                name=f"{name}.{type_image.split('/')[-1]}"
            )
        except Exception:
            raise ValidationError('image is no valid')

    def check_username(self):
        return User.objects.filter(
            username=self.cleaned_data["username"]
        ).exists()
