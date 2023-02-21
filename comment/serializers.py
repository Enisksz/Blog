from rest_framework import serializers

from comment.models import Comment

class CommentListSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()
    
    class Meta:
        model = Comment
        fields = '__all__'

    def get_replies(self,obj):
        if obj.any_children:
            return CommentListSerializer(obj.children(),many=True).data

class CommentCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        exclude = ['created_on',]

    def validate(self, attrs):
        if attrs['parent']:
            if attrs['parent'].post != attrs['post']:
                raise serializers.ValidationError('something went wrong')
        return attrs
    
class CommentUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
    
    def update(self,instance,validated_data):
        instance.user = validated_data['user']
        instance.content = validated_data['content']
        instance.post = validated_data['post']
        instance.save()
        return instance

class CommentDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'