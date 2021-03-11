from instagram.models import Post
from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "name", "avatar_url"]


class PostSerializer(ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Post
        fields = "__all__"