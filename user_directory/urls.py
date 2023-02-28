from django.urls import path
from rest_framework import routers
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from user_directory.views import LocationsViewSet, UsersView, UserDetailView, UserCreateView, UserUpdateView, \
    UserDeleteView

router = routers.SimpleRouter()
router.register('locations', LocationsViewSet)

urlpatterns = [
    path("users/", UsersView.as_view()),
    path("users/<int:pk>/", UserDetailView.as_view()),
    path("users/create/", UserCreateView.as_view()),
    path("users/update/<int:pk>/", UserUpdateView.as_view()),
    path("users/delete/<int:pk>/", UserDeleteView.as_view()),
    path("login/", views.obtain_auth_token),
    path("token/", TokenObtainPairView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view())
]

urlpatterns += router.urls