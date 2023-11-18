from django.urls import path

from usermovierecommend.views.user_views import UserView
from usermovierecommend.views.movie_views import MovieView

urlpatterns = [
    path('create-user/', UserView.as_view(), name='create-user'),
    path('all-users/', UserView.as_view(), name='list-users'),
    path('update-user/<int:user_id>/', UserView.as_view(), name='update-user'),
    path('delete-user/<int:user_id>/', UserView.as_view(), name='delete-user'),
    path('create-movie/', MovieView.as_view(), name='create-user'),
    path('all-movies/', MovieView.as_view(), name='list-users'),
    path('update-movie/<int:movie_id>/', MovieView.as_view(), name='update-user'),
    path('delete-movie/<int:movie_id>/', MovieView.as_view(), name='delete-user')
]