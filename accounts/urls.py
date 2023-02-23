from django.urls import path
from .views import RegisterUserAPIView,ChangePasswordAPIView

urlpatterns = [
    path('register/',RegisterUserAPIView.as_view(),name='register'),
    path('change-password/',ChangePasswordAPIView.as_view(),name='change-password'),
]