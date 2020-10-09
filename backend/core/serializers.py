from rest_framework.serializers import ModelSerializer

from .models import User, UserVideoItem


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class UserVideoItemSerializer(ModelSerializer):

    class Meta:
        model = UserVideoItem
        fields = '__all__'
