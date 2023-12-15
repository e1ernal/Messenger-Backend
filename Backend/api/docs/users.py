from drf_yasg import openapi
from rest_framework import status

USER_CREATE = {
    'manual_parameters': [
        openapi.Parameter('first_name', openapi.IN_QUERY,
                          description="Имя пользователя",
                          type=openapi.TYPE_STRING,
                          required=True),
        openapi.Parameter('last_name', openapi.IN_QUERY,
                          description="Фаимилия пользователя",
                          type=openapi.TYPE_STRING,
                          required=False),
    ],
    "responses": {
        status.HTTP_200_OK: openapi.Response(
            "Success",
            examples={
                "application/json": {
                    "token": "Токен пользователя"
                }
            },
        )
    },
}

USER_ME = {
    "responses": {
        status.HTTP_200_OK: openapi.Response(
            "Success",
            examples={
                "application/json": {
                    "id": "1",
                    "first_name": "Egor",
                    "last_name": "Egorov",
                    "phone_number": "+79991113344",
                    "image": "/uploads/colorings/index.jpg"
                }
            },
        )
    },
}
