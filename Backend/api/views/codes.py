from drf_yasg.utils import swagger_auto_schema

from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from service_objects.errors import InvalidInputsError

from api.docs.codes import VERIFICATION_CODES, VERIFICATION_CODES_CONFIEM
from api.serializers.codes.serializers import VerificationCodeSerializer, TokenSerializer
from api.services.code.confirm import CodeConfirmService
from api.services.code.create import CodeCreateService


class VerificationCodeCreateView(APIView):

    @swagger_auto_schema(**VERIFICATION_CODES)
    def post(self, request, *args, **kwargs):
        try:
            outcome = CodeCreateService.execute({
                'phone_number': request.data.get('phone_number'),
                'request': request
            })
            request = outcome.data['request']
            return Response(VerificationCodeSerializer(outcome).data, status=status.HTTP_201_CREATED)
        except InvalidInputsError as error:
            return Response(error.errors, status=status.HTTP_400_BAD_REQUEST)


class VerificationCodeConfirmView(APIView):

    @swagger_auto_schema(**VERIFICATION_CODES_CONFIEM)
    def post(self, request, *args, **kwargs):
        try:
            outcome = CodeConfirmService.execute({
                'code': request.data.get('code'),
                'request': request
            })
            if hasattr(outcome, 'token'):
                return Response(TokenSerializer(outcome).data, status=status.HTTP_200_OK)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except InvalidInputsError as error:
            return Response(error.errors, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError as error:
            return Response({
                'error': error.detail
            }, status=status.HTTP_400_BAD_REQUEST)
