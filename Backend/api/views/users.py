import base64
from datetime import datetime

from django.core.files.base import ContentFile
from django.db.models import Q
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.docs.users import USER_CREATE, USER_ME, USER_USERNAME
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
                    'error': 'first_name обязательное поле'
                }, status=status.HTTP_400_BAD_REQUEST)
            if not request.data.get('username'):
                return Response({
                    'error': 'username обязательное поле'
                }, status=status.HTTP_400_BAD_REQUEST)
            if not request.data.get('image'):
                return Response({
                    'error': 'image обязательное поле'
                }, status=status.HTTP_400_BAD_REQUEST)
            image = self.convert_base64_to_image(request.data['image'])
            user = User.objects.filter(
                Q(username=request.data['username']) |
                Q(phone_number=request.data['phone_number'])
            )
            if user.exists():
                return Response({
                    'error': 'Пользователь с таким номером телефона или никнеймом уже сущетсвует'
                }, status=status.HTTP_400_BAD_REQUEST)
            params = {
                'username': request.data['username'],
                'first_name': request.data['first_name'],
                'last_name': request.data.get('last_name', ' '),
                'phone_number': request.session['phone_number'],
                'image': image
            }
            user = User.objects.create_user(**params)
            del request.session[request.session['phone_number']]
            del request.session['phone_number']
            del request.session['response']
            return Response({'token': str(user.auth_token)}, status=status.HTTP_201_CREATED)
        return Response({
            'error': 'Сначала подтвержите свой номер'
        }, status=status.HTTP_400_BAD_REQUEST)


class UserMeDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(**USER_ME)
    def get(self, request, *args, **kwargs):
        return Response(UserSerializer(request.user).data, status=status.HTTP_200_OK)


class UserUsernameCheckView(APIView):

    @swagger_auto_schema(**USER_USERNAME)
    def get(self, request, *args, **kwargs):
        if not request.query_params.get('username'):
            return Response({
                'error': 'username обязательное поле'
            }, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.filter(username=request.query_params['username'])
        if user.exists():
            return Response({
                'username': 'Никнейм занят',
            }, status=status.HTTP_400_BAD_REQUEST)
        return Response({
            'username': 'Никнейм свободен'
        })
