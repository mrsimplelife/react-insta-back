from instagram.serializers import PostSerializer
from instagram.models import Post
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]
