from django.db import models
from blog.models import Post
from django.contrib.auth.models import User
# Create your models here.

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name='reviews')
    content = models.TextField()
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='replies')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Comment {} by {}'.format(self.content, self.user.username)

    class Meta:
        ordering = ['created_on']
    
    def children(self):
        return Comment.objects.filter(parent=self)
    
    @property
    def any_children(self):
        return Comment.objects.filter(parent=self).exists()