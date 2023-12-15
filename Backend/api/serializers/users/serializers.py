from rest_framework import serializers

from models_app.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'phone_number',
            'first_name',
            'last_name',
            'image'
        )