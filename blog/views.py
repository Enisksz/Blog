from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner
from .serializers import PostListSerializer,PostCreateSerializer,PostUpdateSerializer,PostDeleteSerializer

from blog.models import Post
# Create your views here.

class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer

class PostCreateAPIView(CreateAPIView):
    model = Post
    serializer_class = PostCreateSerializer
    permission_classes = [IsAuthenticated,IsOwner]

class PostUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostUpdateSerializer
    permission_classes = [IsAuthenticated,IsOwner]
    lookup_field = 'pk'

class PostDeleteAPIView(RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDeleteSerializer
    permission_classes = [IsOwner,IsAuthenticated]
    lookup_field = 'pk'