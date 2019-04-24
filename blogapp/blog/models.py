from django.db import models

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to = 'images/')
    description = models.TextField()
    author = models.CharField(max_length=250)
