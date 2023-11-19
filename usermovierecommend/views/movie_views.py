from django.http import JsonResponse
from rest_framework import generics
from usermovierecommend.services.movie_services import MovieService


class MovieView(generics.CreateAPIView, generics.ListAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    def post(self, request, *args, **kwargs):
        movie_data = request.data
        created_movie_data = MovieService.create_movie(movie_data)
        return JsonResponse({
            "message": "Movie Creation Api",
            "movie_data": created_movie_data
        })

    def get(self, request, *args, **kwargs):
        movies = MovieService.get_all_movies()
        return JsonResponse({
            "message": "All Movies",
            "movie": movies
        })

    def put(self, request, *args, **kwargs):
        movie_id = kwargs.get('movie_id')
        updated_data = request.data
        updated_movie_data = MovieService.update_movies(movie_id, updated_data)
        if updated_movie_data:
            return JsonResponse({
                "message": "Update Movie",
                "movie_data": updated_movie_data
            })
        else:
            return JsonResponse({
                "message": f"Movie {movie_id} Not Found"
            }, status=404)

    def delete(self, request, *args, **kwargs):
        movie_id = kwargs.get('movie_id')
        if MovieService.delete_movie(movie_id):
            return JsonResponse({
                "message": f"Movie {movie_id} deleted"
            })
        else:
            return JsonResponse({
                "message": f"Movie {movie_id} Not Found"
            }, status=404)
