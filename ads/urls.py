from django.urls import path
from ads import views


urlpatterns = [
    path("ads/", views.AdsListView.as_view()),
    path("ads/create/", views.AdCreateView.as_view()),
    path('ads/<int:pk>/', views.AdDetailView.as_view()),
    path('ads/<int:pk>/upload_image/', views.AdUpdateView.as_view()),
    path("ads/update/<int:pk>/", views.AdUpdateView.as_view()),
    path("ads/delete/<int:pk>/", views.AdDeleteView.as_view()),
    path('category/', views.CategoriesListView.as_view()),
    path('category/<int:pk>/', views.CategoryDetailView.as_view()),
    path("category/create/", views.CategoryCreateView.as_view()),
    path("category/update/<int:pk>/", views.CategoryUpdateView.as_view()),
    path("category/delete/<int:pk>/", views.CategoryDeleteView.as_view()),
    path("collections/", views.CollectionView.as_view()),
    path("collections/create/", views.CollectionCreateView.as_view()),
    path("collections/<int:pk>/", views.CollectionDetailView.as_view()),
    path("collections/update/<int:pk>/", views.CollectionUpdateView.as_view()),
    path("collections/delete/<int:pk>/", views.CollectionDeleteView.as_view())

]