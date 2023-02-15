from django.urls import path
from rest_framework import routers
from user_directory import views
from user_directory.views import LocationsViewSet

router = routers.SimpleRouter()
router.register('locations', LocationsViewSet)

urlpatterns = [
    path("users/", views.UsersView.as_view()),
    path("users/<int:pk>/", views.UserDetailView.as_view()),
    path("users/create/", views.UserCreateView.as_view()),
    path("users/update/<int:pk>/", views.UserUpdateView.as_view()),
    path("users/delete/<int:pk>/", views.UserDeleteView.as_view()),
]

urlpatterns += router.urls