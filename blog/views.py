from .models import *
from users.models import UserProfile
from .serializers import *
from users.serializers import UserProfileSerializer
from rest_framework import viewsets

# Create your views here.
class BlogPostViews(viewsets.ModelViewSet):
    queryset=BlogPost.objects.all()
    serializer_class=BlogPostSerializer
    
class TagViews(viewsets.ModelViewSet):
    queryset=Tag.objects.all()
    serializer_class=TagSerializer

class CategoryView(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer


class CommentViews(viewsets.ModelViewSet):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer