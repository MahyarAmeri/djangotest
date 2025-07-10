from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class massage(models.Model):
    sender = models.ForeignKey(User,on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User,on_delete=models.CASCADE, related_name='receiver')
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)


class CountView(models.Model):
    count = models.IntegerField(default=0)