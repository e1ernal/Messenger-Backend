from rest_framework import serializers

from models_app.models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = (
            'author',
            'direct',
            'text',
            'created_at',
            'updated_at'
        )
