from django.db import models
from twitteruser.models import MyUser
from tweet.models import TweetModel
# Create your models here.


class NoteModle(models.Model):
    the_tweet = models.ForeignKey(TweetModel, on_delete=models.CASCADE)
    the_users = models.ManyToManyField(MyUser, symmetrical=False)
