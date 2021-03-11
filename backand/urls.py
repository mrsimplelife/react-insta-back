from typing import List, Union
from django.conf import settings
from django.contrib import admin
from django.urls import URLPattern, URLResolver, include, path
from django.conf.urls.static import static
from django_pydenticon.views import image as pydenticon_image

urlpatterns: List[Union[URLPattern, URLResolver]] = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("", include("instagram.urls")),
    path("identicon/image/<path:data>.png", pydenticon_image, name="pydenticon_image"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    import debug_toolbar

    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]
