from django.shortcuts import render
from django.views import View
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from service_objects.errors import InvalidInputsError

from api.docs.users import USER_CREATE, USER_ME, USER_USERNAME, USER_SEARCH, USER_UPDATE
from api.serializers import UserSerializer, UserUpdateSerializer
from api.serializers.codes.serializers import TokenSerializer
from api.services.user.check_username import UserCheckUsernameService
from api.services.user.create import UserCreateService
from api.services.user.delete import UserDeleteService
from api.services.user.search import UserSearchService
from api.services.user.update import UserUpdateService


class UserCreateView(APIView):

    @swagger_auto_schema(**USER_CREATE)
    def post(self, request, *args, **kwargs):
        if request.session.get('phone_number'):
            try:
                outcome = UserCreateService.execute({
                    'username': request.data.get('username'),
                    'first_name': request.data.get('first_name'),
                    'last_name': request.data.get('last_name'),
                    'image': request.data.get('image'),
                    'request': request,
                })
                request = outcome.data['request']
                return Response(TokenSerializer(outcome).data,
                                status=status.HTTP_201_CREATED)
            except InvalidInputsError as error:
                return Response(error.errors, status=status.HTTP_400_BAD_REQUEST)
            except ValidationError as error:
                return Response({
                    'error': error.detail
                }, status=status.HTTP_400_BAD_REQUEST)
        return Response({
            'error': 'Сначала подтвердите свой номер'
        }, status=status.HTTP_400_BAD_REQUEST)


class UserDeleteView(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request, *args, **kwargs):
        UserDeleteService.execute({
            'user': request.user
        })
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserUpdateView(APIView):
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(**USER_UPDATE)
    def patch(self, request, *args, **kwargs):
        try:
            outcome = UserUpdateService.execute({
                'user': request.user,
                'username': request.data.get('username'),
                'first_name': request.data.get('first_name'),
                'last_name': request.data.get('last_name'),
                'image': request.data.get('image')
            })
            return Response(UserUpdateSerializer(outcome).data, status=status.HTTP_200_OK)
        except InvalidInputsError as error:
            return Response(error.errors, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError as error:
            return Response({
                'error': error.detail
            }, status=status.HTTP_400_BAD_REQUEST)


class UserMeDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(**USER_ME)
    def get(self, request, *args, **kwargs):
        return Response(UserSerializer(request.user).data, status=status.HTTP_200_OK)


class UserUsernameCheckView(APIView):

    @swagger_auto_schema(**USER_USERNAME)
    def get(self, request, *args, **kwargs):
        try:
            UserCheckUsernameService.execute({
                'username': request.query_params.get('username')
            })
            return Response({
                'username': 'Никнейм свободен',
            }, status=status.HTTP_200_OK)
        except InvalidInputsError as error:
            return Response(error.errors, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError as error:
            return Response({
                'error': error.detail
            }, status=status.HTTP_400_BAD_REQUEST)


class UserSearchView(APIView):
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(**USER_SEARCH)
    def get(self, request, *args, **kwargs):
        try:
            outcome = UserSearchService.execute({
                'search': request.query_params.get('search'),
                'user': request.user
            })
            return Response(
                UserSerializer(outcome, many=True).data,
                status=status.HTTP_200_OK
            )
        except InvalidInputsError as error:
            return Response(error.errors, status=status.HTTP_400_BAD_REQUEST)


class HomePageRenderView(View):

    def get(self, request, pk):
        return render(request, 'index.html', context={
            'pk': pk
        })
