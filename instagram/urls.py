from django.urls import include, path
from instagram import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("posts", views.PostViewSet)

urlpatterns = [path("api/", include(router.urls))]
