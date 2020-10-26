from rest_framework.serializers import ModelSerializer

from .models import UserVideoItem


class UserVideoItemSerializer(ModelSerializer):

    class Meta:
        model = UserVideoItem
        fields = '__all__'
