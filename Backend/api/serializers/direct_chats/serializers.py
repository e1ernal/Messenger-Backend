from rest_framework import serializers

from models_app.models import DirectChat, User


class DirectChatSerializer(serializers.ModelSerializer):
    chat_id = serializers.IntegerField(source='id')
    username = serializers.CharField(source='second_user.username')
    image = serializers.ImageField(source='second_user.image')

    class Meta:
        model = DirectChat
        fields = (
            'chat_id',
            'username',
            'image'
        )


class DirectChatListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'image'
        )
