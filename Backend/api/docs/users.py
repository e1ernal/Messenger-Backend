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
        openapi.Parameter('image', openapi.IN_QUERY,
                          description="Фото",
                          type=openapi.TYPE_STRING,
                          required=True),
        openapi.Parameter('username', openapi.IN_QUERY,
                          description="Никнейм пользователя",
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
                    "username": "egor4ick",
                    "last_name": "Egorov",
                    "phone_number": "+79991113344",
                    "image": "/uploads/colorings/index.jpg"
                }
            },
        )
    },
}

USER_USERNAME = {
    'manual_parameters': [
        openapi.Parameter('username', openapi.IN_QUERY,
                          description="Никнейм пользователя",
                          type=openapi.TYPE_STRING,
                          required=True),
    ],
    "responses": {
        status.HTTP_200_OK: openapi.Response(
            "Success",
            examples={
                "application/json": {
                    "username": "Никнейм свободен"
                },
            },
        ),
        status.HTTP_400_BAD_REQUEST: openapi.Response(
            "Error",
            examples={
                "application/json": {
                    "username": "Никнейм зянят",
                    "error": "username обязательное поле"
                },
            },
        )
    },
}

USER_SEARCH = {
    'manual_parameters': [
        openapi.Parameter('search', openapi.IN_QUERY,
                          description="Значение для поиска пользователя",
                          type=openapi.TYPE_STRING,
                          required=True),
    ],
    "responses": {
        status.HTTP_200_OK: openapi.Response(
            "Success",
            examples={
                "application/json": [{
                    "id": "1",
                    "first_name": "Egor",
                    "username": "egor4ick",
                    "last_name": "Egorov",
                    "phone_number": "+79991113344",
                    "public_key": "test_public_key",
                    "image": "/uploads/colorings/index.jpg"
                }]
            },
        ),
        status.HTTP_400_BAD_REQUEST: openapi.Response(
            "Error",
            examples={
                "application/json": {
                    "error": "search обязательное поле"
                },
            },
        )
    },
}

USER_UPDATE = {
    'manual_parameters': [
        openapi.Parameter('username', openapi.IN_QUERY,
                          description="Ник пользователя",
                          type=openapi.TYPE_STRING,
                          required=False),
        openapi.Parameter('first_name', openapi.IN_QUERY,
                          description="Имя пользователя",
                          type=openapi.TYPE_STRING,
                          required=False),
        openapi.Parameter('last_name', openapi.IN_QUERY,
                          description="Фамилия пользователя",
                          type=openapi.TYPE_STRING,
                          required=False),
        openapi.Parameter('image', openapi.IN_QUERY,
                          description="Фото пользователя в формате bs64",
                          type=openapi.TYPE_STRING,
                          required=False),
    ],
    "responses": {
        status.HTTP_200_OK: openapi.Response(
            "Success",
            examples={
                "application/json": {
                    "id": "1",
                    "first_name": "Egor",
                    "username": "egor4ick",
                    "last_name": "Egorov",
                    "image": "/uploads/colorings/index.jpg"
                }
            },
        ),
        status.HTTP_400_BAD_REQUEST: openapi.Response(
            "Error",
            examples={
                "application/json": {
                    "error": "ошибка запроса"
                },
            },
        )
    },
}
