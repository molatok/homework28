from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from ads import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home_page),
    path("ads/", views.AdsView.as_view()),
    path("ads/create/", views.AdCreateView.as_view()),
    path('ads/<int:pk>/', views.AdDetailView.as_view()),
    path('ads/<int:pk>/upload_image/', views.AdUpdateView.as_view()),
    path("ads/delete/<int:pk>/", views.AdDeleteView.as_view()),
    path('category/', views.CategoriesListView.as_view()),
    path('category/<int:pk>/', views.CategoryDetailView.as_view()),
    path("category/create/", views.CategoryCreateView.as_view()),
    path("category/update/<int:pk>/", views.CategoryUpdateView.as_view()),
    path("category/delete/<int:pk>/", views.CategoryDeleteView.as_view()),
    path("users/", views.UserView.as_view()),
    path("users/<int:pk>/", views.UserDetailView.as_view()),
    path("users/create/", views.UserCreateView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
