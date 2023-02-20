from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView
from .serializers import PostListSerializer,PostCreateSerializer,PostUpdateSerializer,PostDeleteSerializer

from blog.models import Post
# Create your views here.

class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer

class PostCreateAPIView(CreateAPIView):
    model = Post
    serializer_class = PostCreateSerializer

class PostUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostUpdateSerializer
    lookup_field = 'pk'

class PostDeleteAPIView(RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDeleteSerializer
    lookup_field = 'pk'