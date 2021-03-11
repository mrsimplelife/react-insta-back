from django.urls import include, path
from instagram import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("posts", views.PostViewSet)
router.register(r"posts/(?P<post_pk>\d+)/comments", views.CommentViewSet)

urlpatterns = [path("api/", include(router.urls))]
