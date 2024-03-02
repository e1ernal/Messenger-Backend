from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from service_objects.errors import InvalidInputsError

from api.docs.direct_chats import (DIRECT_CHATS_CREATE, DIRECT_CHATS_DELETE, DIRECT_CHATS_LIST)
from api.serializers.direct_chats.serializers import (DirectChatSerializer, DirectChatListSerializer)
from api.services.direct_chat.create import DirectChatCreateService
from api.services.direct_chat.delete import DirectChatDeleteService
from api.services.direct_chat.list import DirectChatListService


class DirectChatCreateView(APIView):
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(**DIRECT_CHATS_CREATE)
    def post(self, request, *args, **kwargs):
        try:
            outcome = DirectChatCreateService.execute({
                'first_user': request.user,
                'second_user': kwargs['id'],
                'encrypted_key': request.data.get('encrypted_key')
            })
            return Response({
                'interlocutor': DirectChatSerializer(outcome).data
            }, status=status.HTTP_201_CREATED)
        except InvalidInputsError as error:
            return Response(error.errors, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError as error:
            return Response({
                'error': error.detail
            }, status=error.code if hasattr(error, 'code') else status.HTTP_400_BAD_REQUEST)


class DirectChatDeleteView(APIView):
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(**DIRECT_CHATS_DELETE)
    def delete(self, request, *args, **kwargs):
        try:
            DirectChatDeleteService.execute(kwargs | {'user': request.user})
            return Response(status=status.HTTP_204_NO_CONTENT)
        except InvalidInputsError as error:
            return Response(error.errors, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError as error:
            return Response({
                'error': error.detail
            }, status=error.code if hasattr(error, 'code') else status.HTTP_400_BAD_REQUEST)


class DirectChatListView(APIView):
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(**DIRECT_CHATS_LIST)
    def get(self, request, *args, **kwargs):
        outcome = DirectChatListService.execute({'user': request.user})
        return Response({"interlocutors": DirectChatListSerializer(outcome, many=True).data})
