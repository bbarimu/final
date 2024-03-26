from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Movie, Review, Favorite
from .serializers import MovieSerializer, ReviewSerializer, FavoriteSerializer

class MovieList(generics.ListCreateAPIView):
    """Представление для списка всех фильмов и создания новых фильмов."""
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    """Представление для детального просмотра, обновления и удаления фильма."""
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class ReviewList(generics.ListCreateAPIView):
    """Представление для списка всех отзывов к фильму и создания новых отзывов."""
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """Автоматическое присвоение текущего пользователя отзыву."""
        serializer.save(user=self.request.user)

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    """Представление для детального просмотра, обновления и удаления отзыва."""
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class FavoriteList(generics.ListCreateAPIView):
    """Представление для списка всех избранных фильмов пользователя и создания новых избранных фильмов."""
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        """Получение списка избранных фильмов текущего пользователя."""
        user = self.request.user
        return Favorite.objects.filter(user=user)

    def perform_create(self, serializer):
        """Автоматическое присвоение текущего пользователя избранному фильму."""
        serializer.save(user=self.request.user)

class FavoriteDetail(generics.RetrieveUpdateDestroyAPIView):
    """Представление для детального просмотра, обновления и удаления избранного фильма."""
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
