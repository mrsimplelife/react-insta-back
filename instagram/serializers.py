from instagram.models import Comment, Post
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from django.contrib.auth import get_user_model

User = get_user_model()


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "name", "avatar_url"]


class PostSerializer(ModelSerializer):
    author = AuthorSerializer(read_only=True)
    is_like = SerializerMethodField("is_like_field")

    def is_like_field(self, instance):
        user = self.context["request"].user
        return instance.is_like_user(user)

    class Meta:
        model = Post
        fields = [
            "id",
            "author",
            "created_at",
            "photo",
            "caption",
            "location",
            "tag_set",
            "is_like",
        ]


class CommentSerializer(ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "author", "message", "created_at"]
