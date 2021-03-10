from accounts.serializers import SignupSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny


class SignupView(CreateAPIView):
    serializer_class = SignupSerializer
    permission_classes = [AllowAny]
