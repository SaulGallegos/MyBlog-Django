from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # img = models.ImageField()
    date = models.DateField(auto_now_add=True)

    def __str__(self): 
         return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=(str(self.id)))
    





