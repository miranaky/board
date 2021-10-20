from rest_framework import serializers
from users.serializers import TinyUserSerializer
from .models import Post


class ReadPostSerializer(serializers.ModelSerializer):
    """Post Model Serializer"""

    author = TinyUserSerializer()

    class Meta:
        model = Post
        fields = "__all__"


class WritePostSerializer(serializers.ModelSerializer):
    """Post Model Serializer"""

    class Meta:
        model = Post
        fields = (
            "title",
            "content",
        )
