from rest_framework import serializers
from django.utils import timezone
from blog.models import Post

class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','title','content','created','modified','image']

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title','content','image')

    def create(self, validated_data):
        post = Post(
            title = validated_data['title'],
            content = validated_data['content'],
            image = validated_data['image']
        )
        post.save()
        return post

class PostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title','content','image')
    
    def update(self,instance,validated_data):
        instance.title = validated_data['title']
        instance.content = validated_data['content']
        instance.image = validated_data['image']
        instance.save()
        return instance
    
class PostDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
    