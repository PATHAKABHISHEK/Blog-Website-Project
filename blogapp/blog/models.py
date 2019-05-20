from django.db import models

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=250)
    image = models.CharField(max_length = 250)
    description = models.TextField()
    author = models.CharField(max_length=250)
