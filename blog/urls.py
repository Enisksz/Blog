from django.urls import path
from .views import PostListAPIView,PostCreateAPIView,PostUpdateAPIView,PostDeleteAPIView

urlpatterns = [
    path('list/',PostListAPIView.as_view(),name='list'),
    path('create/',PostCreateAPIView.as_view(),name='create'),
    path('update/<int:pk>',PostUpdateAPIView.as_view(),name='update'),
    path('delete/<int:pk>',PostDeleteAPIView.as_view(),name='delete'),
]