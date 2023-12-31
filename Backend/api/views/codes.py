import requests
from drf_yasg.utils import swagger_auto_schema

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.docs.codes import VERIFICATION_CODES, VERIFICATION_CODES_CONFIEM
from api.utils import generate_code
from api.smsc_api import SMSC_LOGIN, SMSC_PASSWORD
from models_app.models import User


class VerificationCodeCreateView(APIView):

    @swagger_auto_schema(**VERIFICATION_CODES)
    def post(self, request, *args, **kwargs):
        if not request.data.get('phone_number'):
            return Response({
                'error': 'phone_number обязательное поле'
            }, status=status.HTTP_400_BAD_REQUEST)
        code = generate_code()
        response = requests.get(
            f'https://smsc.ru/sys/send.php?login={SMSC_LOGIN}&psw={SMSC_PASSWORD}&phones={request.data["phone_number"]}&mes={code}')
        request.session['phone_number'] = request.data['phone_number']
        request.session[request.session['phone_number']] = code
        return Response({'code': code}, status=status.HTTP_200_OK)


class VerificationCodeConfirmView(APIView):

    @swagger_auto_schema(**VERIFICATION_CODES_CONFIEM)
    def post(self, request, *args, **kwargs):
        if not request.session.get('phone_number'):
            return Response({
                'error': 'Сначала нужно отправить код подтверждения на ваш номер телефона'
            }, status=status.HTTP_400_BAD_REQUEST)
        if not request.data.get('code'):
            return Response({
                'error': 'code обязательное поле'
            }, status=status.HTTP_400_BAD_REQUEST)
        if request.session[request.session['phone_number']] != request.data['code']:
            return Response({
                'error': 'Не верный код подтверждения'
            }, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.filter(phone_number=request.session['phone_number'])
        if user.exists():
            return Response({
                'token': str(user.first().auth_token)
            })
        request.session['response'] = True
        return Response({
            'response': request.session['response']
        })
