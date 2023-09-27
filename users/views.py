from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import *
from .serializers import UserSerializer, UserProfileSerializer

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserProfileView(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer