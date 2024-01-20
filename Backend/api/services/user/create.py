import base64
from datetime import datetime
from django import forms
from django.core.files.base import ContentFile
from django.db.models import Q
from rest_framework.exceptions import ValidationError
from service_objects.services import Service

from models_app.models import User


class UserCreateService(Service):
    username = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField(required=False)
    image = forms.CharField()

    def process(self):
        self.check_user_presence()
        self.cleaned_data['image'] = self.convert_base64_to_image(self.cleaned_data['image'])
        user = self.create_user()
        self.token = user.auth_token.key
        self.delete_session()
        return self

    def create_user(self):
        return User.objects.create_user(
            username=self.cleaned_data['username'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data.get('last_name', ' '),
            phone_number=self.data['request'].session['phone_number'],
            image=self.cleaned_data['image']
        )

    def delete_session(self):
        del self.data['request'].session[self.data['request'].session['phone_number']]
        del self.data['request'].session['phone_number']

    def check_user_presence(self):
        user = User.objects.filter(
            Q(username=self.cleaned_data['username']) |
            Q(phone_number=self.data['request'].session['phone_number'])
        )
        if user.exists():
            raise ValidationError('User exists')

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
