from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Posts(models.Model):
    title=models.CharField(max_length=120)
    content=models.TextField()
    date_posted=models.DateField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
