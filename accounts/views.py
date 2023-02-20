from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .serializers import RegisterUserSerializer

from django.contrib.auth.models import User
# Create your views here.

class RegisterUserAPIView(CreateAPIView):
    serializer_class = RegisterUserSerializer