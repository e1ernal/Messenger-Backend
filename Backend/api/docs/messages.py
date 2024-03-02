from drf_yasg import openapi
from rest_framework import status

MESSAGE_CREATE = {
    'manual_parameters': [
        openapi.Parameter('id', openapi.IN_PATH,
                          description="id чата в котором хотим добавить сообщение",
                          type=openapi.TYPE_INTEGER,
                          required=True),
        openapi.Parameter('text', openapi.IN_PATH,
                          description="сообщение (передается в body)",
                          type=openapi.TYPE_INTEGER,
                          required=True),
    ],
    "responses": {
        status.HTTP_201_CREATED: openapi.Response(
            "Success",
            examples={
                "application/json": {
                    "author": 1,
                    "direct": 10,
                    "text": "12aaa",
                    "created_at": "2024-03-02T15:06:19.454336Z",
                    "updated_at": "2024-03-02T15:06:19.454336Z"
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
