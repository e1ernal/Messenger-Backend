from rest_framework import serializers


class VerificationCodeSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=5)


class TokenSerializer(serializers.Serializer):
    token = serializers.CharField()
