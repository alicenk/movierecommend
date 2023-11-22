from rest_framework import serializers
from usermovierecommend.models import UserMovie


class UserMovieSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(read_only=True)

    class Meta:
        model = UserMovie
        fields = '__all__'
