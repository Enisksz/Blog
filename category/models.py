from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = 'categories'
    
    def post_count(self):
        return self.postuser.count()

    def __str__(self):
        return self.name