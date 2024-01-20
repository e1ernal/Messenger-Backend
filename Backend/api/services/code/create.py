import requests
from django import forms
from service_objects.services import Service

from api.smsc_api import SMSC_LOGIN, SMSC_PASSWORD
from api.utils import generate_code


class CodeCreateService(Service):
    phone_number = forms.CharField(max_length=12)

    def process(self):
        self.code = self.get_code
        self.send_sms()
        self.set_session()
        return self

    @property
    def get_code(self):
        return generate_code()

    def send_sms(self):
        phone = self.cleaned_data['phone_number']
        response = requests.get(
            f'https://smsc.ru/sys/send.php?login={SMSC_LOGIN}&psw={SMSC_PASSWORD}&phones={phone}&mes={self.code}'
        )
        return response

    def set_session(self):
        self.data['request'].session['phone_number'] = self.cleaned_data['phone_number']
        self.data['request'].session[self.data['request'].session['phone_number']] = self.code
