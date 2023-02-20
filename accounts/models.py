from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(User):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='post',null=True)
    image = models.ImageField(upload_to="profiles",null=True,blank=True)

    class Meta:
        verbose_name = 'Profile'