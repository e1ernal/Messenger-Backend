import datetime
from rest_framework import serializers

from api.serializers import UserUpdateSerializer
from models_app.models import Message


class MessageSerializer(serializers.ModelSerializer):
    author = UserUpdateSerializer()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_created_at(self, obj):
        datetime_obj = datetime.datetime.combine(obj.created_at, datetime.time.min)
        unix_timestamp = int(datetime_obj.timestamp())
        return unix_timestamp

    def get_updated_at(self, obj):
        datetime_obj = datetime.datetime.combine(obj.updated_at, datetime.time.min)
        unix_timestamp = int(datetime_obj.timestamp())
        return unix_timestamp

    class Meta:
        model = Message
        fields = (
            'author',
            'direct',
            'text',
            'created_at',
            'updated_at'
        )
