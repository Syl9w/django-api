from django.contrib.auth import get_user_model
from rest_framework import generics, viewsets
from .models import Post
from .serializers import PostSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly
# Create your views here.

#Viewsets
class PostViewSet(viewsets.ModelViewSet): # new 
    permission_classes = (IsAuthorOrReadOnly,) 
    queryset = Post.objects.all() 
    serializer_class = PostSerializer
    
class UserViewSet(viewsets.ModelViewSet): # new 
    queryset = get_user_model().objects.all() 
    serializer_class = UserSerializer

#classical views
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
   
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly,)
    

class UserList(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer