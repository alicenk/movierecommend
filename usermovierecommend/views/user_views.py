from django.http import JsonResponse
from rest_framework import generics
from usermovierecommend.services.user_services import UserService


class UserView(generics.CreateAPIView, generics.ListAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    def post(self, request, *args, **kwargs):
        user_data = request.data
        created_user_data = UserService.create_user(user_data)
        return JsonResponse({
            "message": "User Created",
            "user_data": created_user_data
        })

    def get(self, request, *args, **kwargs):
        users = UserService.get_all_users()
        return JsonResponse({
            "message": "All Users",
            "user": users
        })

    def put(self, request, *args, **kwargs):
        user_id = kwargs.get('user_id')
        updated_data = request.data
        updated_user_data = UserService.update_users(user_id, updated_data)
        if updated_user_data:
            return JsonResponse({
                "message": "Update User",
                "user_data": updated_user_data
            })
        else:
            return JsonResponse({
                "message": f"User {user_id} Not Found"
            }, status=404)

    def delete(self, request, *args, **kwargs):
        user_id = kwargs.get('user_id')
        if UserService.delete_user(user_id):
            return JsonResponse({
                "message": f"User {user_id} deleted"
            })
        else:
            return JsonResponse({
                "message": f"User {user_id} Not Found"
            }, status=404)



