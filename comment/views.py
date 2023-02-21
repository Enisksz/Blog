from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializers import CommentListSerializer

from comment.models import Comment

# Create your views here.

class CommentListAPIView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentListSerializer
