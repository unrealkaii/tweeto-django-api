from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tweet(models.Model):
    """
    Represents the tweet object
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=140)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_created',)

    def __str__(self):
        return self.body


class Reply(models.Model):
    """
    Represents the Reply object
    """
    tweet = models.ForeignKey(Tweet, related_name='replies', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=140)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_created',)
    

    def __str__(self):
        return self.body


class Like(models.Model):
    """
    Represents Likes given to Tweet and Reply 
    """
    tweet = models.ForeignKey(Tweet, related_name='likes', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_created',)

    def __str__(self):
        return '{} liked {}'.format(self.author, self.tweet)
