from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Модель для хранения информации о жанрах фильмов
class Genre(models.Model):
    name = models.CharField(max_length=100)  # Название жанра
    
    def __str__(self):
        return self.name

# Модель для хранения информации о режиссерах фильмов
class Director(models.Model):
    name = models.CharField(max_length=100)  # Имя режиссера

    def __str__(self):
        return self.name

# Модель для хранения информации об актерах, снимавшихся в фильмах
class Actor(models.Model):
    name = models.CharField(max_length=100)  # Имя актера

    def __str__(self):
        return self.name

# Модель для хранения информации о странах производства фильмов
class Country(models.Model):
    name = models.CharField(max_length=100)  # Название страны

    def __str__(self):
        return self.name

# Модель для хранения информации о киностудиях или компаниях, которые произвели фильм
class Company(models.Model):
    name = models.CharField(max_length=100)  # Название киностудии

    def __str__(self):
        return self.name

# Модель для хранения информации о фильмах
class Movie(models.Model):
    title = models.CharField(max_length=255)  # Название фильма
    release_year = models.PositiveIntegerField()  # Год выпуска фильма
    description = models.TextField()  # Описание фильма
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)  # Рейтинг фильма
    duration_minutes = models.PositiveIntegerField()  # Продолжительность фильма в минутах
    genres = models.ManyToManyField(Genre)  # Жанры фильма
    directors = models.ManyToManyField(Director)  # Режиссеры фильма
    actors = models.ManyToManyField(Actor)  # Актеры фильма
    country = models.ForeignKey(Country, on_delete=models.CASCADE)  # Страна производства фильма
    company = models.ForeignKey(Company, on_delete=models.CASCADE)  # Киностудия, производившая фильм

    def __str__(self):
        return self.title

# Модель для хранения отзывов пользователей о фильме
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Пользователь, оставивший отзыв
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)  # Фильм, к которому относится отзыв
    rating = models.PositiveIntegerField()  # Оценка фильма
    comment = models.TextField(blank=True)  # Комментарий пользователя к фильму

    def __str__(self):
        return f'{self.user.username} - {self.movie.title}'

# Модель для хранения информации о фильмах, добавленных пользователем в избранное
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Пользователь, добавивший фильм в избранное
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)  # Фильм, добавленный в избранное

    def __str__(self):
        return f'{self.user.username} - {self.movie.title}'