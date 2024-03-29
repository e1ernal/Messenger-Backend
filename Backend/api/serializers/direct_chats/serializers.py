import datetime

from rest_framework import serializers

from models_app.models import DirectChat, User


class DirectChatSerializer(serializers.ModelSerializer):
    chat_id = serializers.IntegerField(source='id')
    first_name = serializers.CharField(source='second_user.first_name')
    last_name = serializers.CharField(source='second_user.last_name')
    username = serializers.CharField(source='second_user.username')
    image = serializers.ImageField(source='second_user.image')

    class Meta:
        model = DirectChat
        fields = (
            'first_name',
            'last_name',
            'chat_id',
            'username',
            'image'
        )


class DirectChatListSerializer(serializers.ModelSerializer):
    last_message = serializers.CharField(source='last_message.text', default=None)
    last_message_created = serializers.DateTimeField(source='last_message.created_at')
    direct_id = serializers.IntegerField()

    # def get_last_message_created(self, obj):
    #     if obj.last_message:
    #         datetime_obj = datetime.datetime.combine(obj.last_message.created_at, datetime.time.min)
    #         unix_timestamp = int(datetime_obj.timestamp())
    #         return unix_timestamp
    #     return None

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'image',
            'last_message',
            'last_message_created',
            'direct_id'
        )
