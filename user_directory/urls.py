from django.urls import path
from user_directory import views

urlpatterns = [
    path("users/", views.UsersView.as_view()),
    path("users/<int:pk>/", views.UserDetailView.as_view()),
    path("users/create/", views.UserCreateView.as_view()),
    path("users/update/<int:pk>/", views.UserUpdateView.as_view()),
    path("users/delete/<int:pk>/", views.UserDeleteView.as_view()),
    path("locations/", views.LocationsView.as_view()),
    path("locations/<int:pk>/", views.LocationDetailView.as_view()),
    path("locations/delete/<int:pk>/", views.LocationDeleteView.as_view()),
    path("locations/create/", views.LocationCreateView.as_view()),
    path("locations/update/<int:pk>/", views.LocationUpdateView.as_view()),
]