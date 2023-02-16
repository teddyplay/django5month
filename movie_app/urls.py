from django.urls import path
from . import views


urlpatterns = [
    path('api/v1/directors/', views.director_view),
    path('api/v1/directors/<int:id>/', views.get_director),
    path('api/v1/movies/', views.list_movies),
    path('api/v1/movies/<int:id>/', views.get_movies),
    path('api/v1/reviews/', views.list_review),
    path('api/v1/reviews/<int:id>/', views.get_review),
]

