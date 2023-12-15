import base64
from datetime import datetime

from django.core.files.base import ContentFile
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.docs.users import USER_CREATE, USER_ME
from api.serializers import UserSerializer
from models_app.models import User


class UserCreateView(APIView):

    @staticmethod
    def convert_base64_to_image(image):
        type_image, image = image.split(';base64,')
        name = datetime.now().strftime("%Y%m%d%H%M%S")
        return ContentFile(
            base64.b64decode(image),
            name=f"{name}.{type_image.split('/')[-1]}"
        )

    @swagger_auto_schema(**USER_CREATE)
    def post(self, request, *args, **kwargs):
        if request.session.get('response'):
            if not request.data.get('first_name'):
                return Response({
                    'error': 'first_name пользователя обязательное поле'
                }, status=status.HTTP_400_BAD_REQUEST)
            if not request.data.get('image'):
                return Response({
                    'error': 'image обязательное поле'
                }, status=status.HTTP_400_BAD_REQUEST)
            image = self.convert_base64_to_image(request.data['image'])
            params = {
                'username': request.data['first_name'],
                'first_name': request.data['first_name'],
                'last_name': request.data.get('last_name', ' '),
                'phone_number': request.session['phone_number'],
                'image': image
            }
            user = User.objects.create_user(**params)
            token = Token.objects.create(user=user).key
            del request.session[request.session['phone_number']]
            del request.session['phone_number']
            del request.session['response']
            return Response({'token': token}, status=status.HTTP_201_CREATED)
        return Response({
            'error': 'Сначала подтвержите свой номер'
        }, status=status.HTTP_400_BAD_REQUEST)


class UserMeDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(**USER_ME)
    def get(self, request, *args, **kwargs):
        return Response(UserSerializer(request.user).data, status=status.HTTP_200_OK)
