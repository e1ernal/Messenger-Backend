from django import forms
from rest_framework.exceptions import ValidationError
from service_objects.services import Service

from models_app.models import User


class CodeConfirmService(Service):
    code = forms.CharField(max_length=5)

    def process(self):
        self.check_phone_number()
        self.check_code()
        user = self.user_presence
        if user.exists():
            self.token = user.first().auth_token.key
            self.token_obj = user.first().auth_token
        return self

    @property
    def user_presence(self):
        return User.objects.filter(phone_number=self.data['request'].session['phone_number'])

    def check_phone_number(self):
        if not self.data['request'].session.get('phone_number'):
            raise ValidationError('Сначала нужно отправить код подтверждения на ваш номер телефона')

    def check_code(self):
        if self.data['request'].session[self.data['request'].session['phone_number']] != self.cleaned_data['code']:
            raise ValidationError('Не верный код подтверждения')
