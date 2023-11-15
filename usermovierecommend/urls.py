from django.urls import path

from usermovierecommend.views.user_views import UserView

urlpatterns = [
    path('create-user/', UserView.as_view(), name='create-user'),
    path('all-users/', UserView.as_view(), name='list-users'),
    path('update-user/<int:user_id>/', UserView.as_view(), name='update-user'),
    path('delete-user/<int:user_id>/', UserView.as_view(), name='delete-user')
]