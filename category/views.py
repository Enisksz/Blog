from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Category
from .serializers import CategoryListSerializer
# Create your views here.

class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer