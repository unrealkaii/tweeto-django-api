from django.contrib import admin
from .models import Tweet, Reply, Like

# Register your models here.

class TweetAdmin(admin.ModelAdmin):
    list_display = ('body', 'author', 'date_created')

class ReplyAdmin(admin.ModelAdmin):
    list_display = ('body', 'author', 'date_created')

class LikeAdmin(admin.ModelAdmin):
    list_display = ('tweet', 'author', 'date_created')

admin.site.register(Tweet, TweetAdmin)
admin.site.register(Reply, TweetAdmin)
admin.site.register(Like, LikeAdmin)
