from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from usermovierecommend.models import UserMovie
from usermovierecommend.models import User
from usermovierecommend.models import Movie
from usermovierecommend.serializers.usermovie_serializer import UserMovieSerializer


class UserMovieServices:

    @staticmethod
    @transaction.atomic
    def create_usermovie(data):

        user = User.objects.get(id=data.get('user_id'))
        movie = Movie.objects.get(id=data.get('movie_id'))

        existing_usermovie = UserMovie.objects.filter(
            user=data.get('user_id'),
            movie=data.get('movie_id')
        ).first()

        if existing_usermovie:
            return {"error": "User Movie exists"}

        usermovie_data = {
            'user': user.id,
            'movie': movie.id
        }
        
        serializer = UserMovieSerializer(data=usermovie_data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        return {"error": "Invalid Data"}
