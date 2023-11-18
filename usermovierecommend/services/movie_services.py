from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction

from usermovierecommend.models import Movie
from usermovierecommend.serializers.movie_serializer import MovieSerializer


class MovieService:
    @staticmethod
    def get_all_movies():
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return serializer.data

    @staticmethod
    def get_movie_by_id(user_id):
        movie = Movie.objects.get(id=movie_id)
        serializer = MovieSerializer(movie)
        return serializer.data

    @staticmethod
    @transaction.atomic
    def create_movie(data):
        existing_movie = Movie.objects.filter(
            name=data.get('name'),
            type=data.get('type')
        ).first()

        if existing_movie:
            return {"error": "Movie exists"}

        serializer = MovieSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        return {"error": "Invalid Data"}

    @classmethod
    def update_movies(cls, movie_id, updated_data):
        movie = Movie.objects.get(id=movie_id)
        serializer = MovieSerializer(movie, data=updated_data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        return None

    @classmethod
    def delete_user(cls, movie_id):
        try:
            movie = Movie.objects.get(id=movie_id)
            movie.delete()
            return True
        except ObjectDoesNotExist:
            return False
