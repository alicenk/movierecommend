from usermovierecommend.models import User
from usermovierecommend.serializers.user_serializer import UserSerializer


class UserService:
    @staticmethod
    def get_all_users():
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return serializer.data

    @staticmethod
    def get_user_by_id(user_id):
        user = User.objects.get(id=user_id)
        serializer = UserSerializer(user)
        return serializer.data

    @staticmethod
    def create_user(data):
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        return None

    @classmethod
    def update_users(cls, user_id, updated_data):
        user = User.objects.get(id=user_id)
        serializer = UserSerializer(user, data=updated_data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        return None

    @classmethod
    def delete_user(cls, user_id):
        user = User.objects.get(id=user_id)
        user.delete()
