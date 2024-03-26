from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import MyUser
from .serializers import UserCreateSerializer, UserProfileSerializer

class UserCreateView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer

class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]  # Требуется аутентификация

    def get_object(self):
        return self.request.user

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
