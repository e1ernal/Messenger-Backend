from drf_yasg import openapi
from rest_framework import status

DIRECT_CHATS_CREATE = {
    'manual_parameters': [
        openapi.Parameter('id', openapi.IN_PATH,
                          description="id пользователя с которым хотим создать чат",
                          type=openapi.TYPE_INTEGER,
                          required=True),
        openapi.Parameter('encrypted_key', openapi.IN_QUERY,
                          description="приватный ключ",
                          type=openapi.TYPE_STRING,
                          required=True),
    ],
    "responses": {
        status.HTTP_201_CREATED: openapi.Response(
            "Success",
            examples={
                "application/json": {
                    "interlocutor": {
                        "chat_id": "1",
                        "first_name": "Egor",
                        "last_name": "Egorov",
                        "image": "/uploads/colorings/index.jpg"
                    }
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
        ),
        status.HTTP_401_UNAUTHORIZED: openapi.Response(
            "Error",
            examples={
                "application/json": {
                    "detail": "авторизация"
                },
            },
        ),
        status.HTTP_404_NOT_FOUND: openapi.Response(
            "Error",
            examples={
                "application/json": {
                    "error": "что-то не нашли"
                },
            },
        )
    },
}

DIRECT_CHATS_DELETE = {
    'manual_parameters': [
        openapi.Parameter('id', openapi.IN_PATH,
                          description="id чата, который мы хотим удалить",
                          type=openapi.TYPE_INTEGER,
                          required=True),
    ],
    "responses": {
        status.HTTP_204_NO_CONTENT: openapi.Response(
            "No content",
        ),
        status.HTTP_400_BAD_REQUEST: openapi.Response(
            "Error",
            examples={
                "application/json": {
                    "error": "ошибка запроса"
                },
            },
        ),
        status.HTTP_401_UNAUTHORIZED: openapi.Response(
            "Error",
            examples={
                "application/json": {
                    "detail": "авторизация"
                },
            },
        ),
        status.HTTP_404_NOT_FOUND: openapi.Response(
            "Error",
            examples={
                "application/json": {
                    "error": "что-то не нашли"
                },
            },
        )
    },
}

DIRECT_CHATS_LIST = {
    "responses": {
        status.HTTP_200_OK: openapi.Response(
            "Success",
            examples={
                "application/json":
                    [
                        {
                            "first_name": "Egor",
                            "last_name": "Egorov",
                            "image": "/uploads/colorings/index.jpg",
                            "last_message": "text",
                            "last_message_created": "2024-03-02 14:54:10.122957+00:00",
                            "direct_id": 9
                        },
                        {
                            "first_name": "Egor",
                            "last_name": "Egorov",
                            "image": "/uploads/colorings/index111.jpg",
                            "last_message": None,
                            "last_message_created": None,
                            "direct_id": 10
                        },
                    ]

            },
        ),
        status.HTTP_401_UNAUTHORIZED: openapi.Response(
            "Error",
            examples={
                "application/json": {
                    "detail": "авторизация"
                },
            },
        ),
    },
}
