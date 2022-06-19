from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    Created_date = models.DateTimeField()
    Published_date = models.DateTimeField()
    
