from rest_framework import serializers
from django.utils import timezone
from blog.models import Post

class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','user','title','content','created','modified','image','category']

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title','user','content','image','category')

    def create(self, validated_data):
        post = Post(
            title = validated_data['title'],
            content = validated_data['content'],
            image = validated_data['image'],
            user = validated_data['user'],
            category = validated_data['category']
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
    