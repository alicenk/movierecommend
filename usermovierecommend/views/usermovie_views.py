from django.http import JsonResponse
from rest_framework import generics
from usermovierecommend.services.usermovie_services import UserMovieServices


class UserMovieView(generics.CreateAPIView, generics.ListAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    def post(self, request, *args, **kwargs):
        usermovie_data = request.data
        created_usermovie_data = UserMovieServices.create_usermovie(usermovie_data)
        return JsonResponse({
            "message": "User Movie Creation Api",
            "usermovie_data": created_usermovie_data
        })
