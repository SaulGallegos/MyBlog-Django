from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

class Post(models.Model):
     title = models.CharField(max_length=255)
     body = models.TextField()
     author = models.ForeignKey(User, on_delete=models.CASCADE)
     img = models.ImageField()
     date = models.DateField(auto_now_add=True)





