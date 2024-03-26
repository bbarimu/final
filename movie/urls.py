from django.urls import path
from .views import (
    MovieList, MovieDetail,
    ReviewList, ReviewDetail,
    FavoriteList, FavoriteDetail,
)

urlpatterns = [
    # URL-маршруты для фильмов
    path('movies/', MovieList.as_view(), name='movie-list-create'),
    path('movies/<int:pk>/', MovieDetail.as_view(), name='movie-detail'),

    # URL-маршруты для отзывов
    path('reviews/', ReviewList.as_view(), name='review-list-create'),
    path('reviews/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),

    # URL-маршруты для избранных фильмов
    path('favorites/', FavoriteList.as_view(), name='favorite-list-create'),
    path('favorites/<int:pk>/', FavoriteDetail.as_view(), name='favorite-detail'),
]