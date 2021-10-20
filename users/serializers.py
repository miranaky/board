from rest_framework import serializers
from .models import User


class TinyUserSerializer(serializers.ModelSerializer):

    """Tiny User Serializer just username"""

    class Meta:
        model = User
        fields = (
            "id",
            "username",
        )


class UserSerializer(serializers.ModelSerializer):

    """User Serializer"""

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name", "email", "password")
        read_only_fields = ("id",)

    def create(self, validated_data):
        password = validated_data.get("password")
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user
