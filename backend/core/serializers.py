from django.contrib.auth.hashers import make_password

from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

    def validate_password(self, value):
        if not value:
            raise serializers.ValidationError("This field is required.")
        return make_password(value)
