from django.contrib import admin
from .models import Genre, Director, Actor, Movie, Review, Favorite, Company, Country
# Регистрация моделей в админке
admin.site.register(Genre)
admin.site.register(Director)
admin.site.register(Actor)
admin.site.register(Movie)
admin.site.register(Review)
admin.site.register(Favorite)
admin.site.register(Company)
admin.site.register(Country)

