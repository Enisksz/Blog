from django.urls import path
from .views import CommentListAPIView

urlpatterns = [
    path('list/',CommentListAPIView.as_view(),name='list'),
]