from rest_framework import serializers
from .models import Genre, Director, Actor, Movie, Review, Favorite, Company , Country

class GenreSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Genre."""

    class Meta:
        model = Genre
        fields = '__all__'

class DirectorSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Director."""

    class Meta:
        model = Director
        fields = '__all__'

class ActorSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Actor."""

    class Meta:
        model = Actor
        fields = '__all__'
    
class CountrySerializer(serializers.ModelSerializer):
    """Сериализатор для модели Country."""

    class Meta:
        model = Country
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
    """Сериализатор для модели Company."""

    class Meta:
        model = Company
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Movie."""
    
    # Включаем вложенные сериализаторы для связанных моделей
    genres = GenreSerializer(many=True, read_only=True) 
    directors = DirectorSerializer(many=True, read_only=True) 
    actors = ActorSerializer(many=True, read_only=True)  
    country = CountrySerializer()
    company = CompanySerializer()


    class Meta:
        model = Movie
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Review."""

    class Meta:
        model = Review
        fields = '__all__'

class FavoriteSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Favorite."""

    class Meta:
        model = Favorite
        fields = '__all__'
