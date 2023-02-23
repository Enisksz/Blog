from django.shortcuts import render
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import CommentListSerializer,CommentCreateSerializer,CommentUpdateSerializer,CommentDeleteSerializer
from comment.models import Comment


# Create your views here.

class CommentListAPIView(ListAPIView):
    #nested commentler gelsin diye override ediyoruz queryseti
    serializer_class = CommentListSerializer

    def get_queryset(self):
        return Comment.objects.filter(parent= None) #parent none demek ilk yorum bunlar demek ve biz bunların altında yorum listelicez

class CommentCreateAPIView(CreateAPIView):

    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer
    permission_classes = [IsAuthenticated,]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CommentUpdateAPIView(RetrieveUpdateAPIView):

    queryset = Comment.objects.all()
    serializer_class = CommentUpdateSerializer
    permission_classes = [IsAuthenticated,]
    lookup_field = 'pk'

class CommentDeleteAPIView(RetrieveDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDeleteSerializer
    permission_classes = [IsAuthenticated,]
    lookup_field = 'pk'