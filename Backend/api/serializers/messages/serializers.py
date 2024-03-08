from rest_framework import serializers

from api.serializers import UserUpdateSerializer
from models_app.models import Message


class MessageSerializer(serializers.ModelSerializer):
    author = UserUpdateSerializer()

    class Meta:
        model = Message
        fields = (
            'author',
            'direct',
            'text',
            'created_at',
            'updated_at'
        )
