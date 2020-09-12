from django.db import models
from twitteruser.models import MyUser
# Create your models here.


class TweetModel(models.Model):
    body = models.TextField(max_length=240)
    time = models.DateField(auto_now=True)
    who_tweeted = models.ForeignKey(
        MyUser, on_delete=models.CASCADE)
