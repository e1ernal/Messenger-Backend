from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from service_objects.errors import InvalidInputsError

from api.serializers.messages.serializers import MessageSerializer
from api.services.message.create import MessageCreateService


class MessageCreateView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        try:
            outcome = MessageCreateService.execute({
                'author': request.user,
                'direct': kwargs['id'],
                'text': request.data.get('text')
            })
            return Response(MessageSerializer(outcome).data,
                            status=status.HTTP_201_CREATED)
        except InvalidInputsError as error:
            return Response(error.errors, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError as error:
            return Response({
                'error': error.detail
            }, status=status.HTTP_400_BAD_REQUEST)