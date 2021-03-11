from accounts.serializers import SignupSerializer, SuggestionUserSerializer
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model


class SignupView(CreateAPIView):
    serializer_class = SignupSerializer
    permission_classes = [AllowAny]


class SuggestionListAPIView(ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = SuggestionUserSerializer
