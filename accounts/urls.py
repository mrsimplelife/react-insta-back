from accounts import views
from django.urls import path
from rest_framework_jwt.views import (
    refresh_jwt_token,
    obtain_jwt_token,
    verify_jwt_token,
)


urlpatterns = [
    path("signup/", views.SignupView.as_view()),
    path("token/", obtain_jwt_token),
    path("token/verify/", verify_jwt_token),
    path("token/refresh/", refresh_jwt_token),
    path(
        "suggestions/",
        views.SuggestionListAPIView.as_view(),
        name="suggestion_user_list",
    ),
    path("follow/", views.user_follow, name="user_follow"),
    path("unfollow/", views.user_unfollow, name="user_unfollow"),
]
