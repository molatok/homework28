from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from ads import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("tests-api/", include('rest_framework.urls')),
    path("", views.home_page),
    path("", include('ads.urls')),
    path('', include('user_directory.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
