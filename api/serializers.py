from rest_framework import serializers
from .models import Tweet, Reply, Like

class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = '__all__'


class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
        
