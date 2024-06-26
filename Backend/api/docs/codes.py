from drf_yasg import openapi
from rest_framework import status

VERIFICATION_CODES = {
    "phone_number": "Номер телефона, на коорый будет приходить код подтверждения. В начале используем маску страны -- +79991111212",
    'manual_parameters': [
        openapi.Parameter('phone_number', openapi.IN_QUERY,
                          description="Номер телефона, на коорый будет приходить код подтверждения. В начале используем маску страны -- +79991111212",
                          type=openapi.TYPE_STRING,
                          required=True),
    ],
    "responses": {
        status.HTTP_201_CREATED: openapi.Response(
            "Success",
            examples={
                "application/json": {
                    "code": "12345"
                }
            },
        )
    },
}

VERIFICATION_CODES_CONFIEM = {
    "code": "Код для подтверждения регистрации по номеру телефона",
    'manual_parameters': [
        openapi.Parameter('code', openapi.IN_QUERY,
                          description="Код для подтверждения регистрации по номеру телефона",
                          type=openapi.TYPE_STRING,
                          required=True),
        openapi.Parameter('public_key', openapi.IN_QUERY,
                          description="Публичный ключ пользователя, который мы хотим ему присвоить",
                          type=openapi.TYPE_STRING,
                          required=True),
    ],
    "responses": {
        status.HTTP_200_OK: openapi.Response(
            "Success",
            examples={
                "application/json": {
                    "token": 'asdasdasdasdasdasdsad'
                }
            },
        ),
        status.HTTP_204_NO_CONTENT: openapi.Response(
            "No content"
        )
    },
}
