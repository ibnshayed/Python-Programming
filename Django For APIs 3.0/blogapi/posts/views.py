from django.contrib.auth import get_user_model
from rest_framework import viewsets, generics, permissions

from .models import Post
from .serializers import PostSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly

# Create your views here.

# Using View Set
class PostViewSet(viewsets.ModelViewSet):
    permission_classes      = (IsAuthorOrReadOnly,)
    queryset                = Post.objects.all()
    serializer_class        = PostSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset                = get_user_model().objects.all()
    serializer_class        = UserSerializer


# Generics API VIEW

# class PostList(generics.ListCreateAPIView):
#     # permission_classes  = (permissions.IsAuthenticated,) # view-level-permission
#     queryset            = Post.objects.all()
#     serializer_class    = PostSerializer

# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     # permission_classes = (permissions.IsAuthenticated,) # view-level-permission
#     permission_classes = (IsAuthorOrReadOnly,) # custom authentications
#     queryset           = Post.objects.all()
#     serializer_class   = PostSerializer

# class UserList(generics.ListCreateAPIView):

#     queryset         = get_user_model().objects.all()
#     serializer_class = UserSerializer

# class UserDetail(generics.RetrieveUpdateDestroyAPIView):

#     queryset         = get_user_model().objects.all()
#     serializer_class = UserSerializer
