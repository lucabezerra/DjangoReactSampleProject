from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import User
from .serializers import UserSerializer


class UserCreateRetrieveView(generics.ListCreateAPIView):
    model = get_user_model()
    serializer_class = UserSerializer

    def get_queryset(self):
        self.queryset = self.model.objects.all()
        return super().get_queryset()

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = []
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()
