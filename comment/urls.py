from django.urls import path
from .views import CommentListAPIView,CommentCreateAPIView,CommentUpdateAPIView,CommentDeleteAPIView

urlpatterns = [
    path('list/',CommentListAPIView.as_view(),name='list'),
    path('create/',CommentCreateAPIView.as_view(),name='create'),
    path('update/<int:pk>',CommentUpdateAPIView.as_view(),name='update'),
    path('delete/<int:pk>',CommentDeleteAPIView.as_view(),name='delete'),
]