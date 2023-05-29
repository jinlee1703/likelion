from django.contrib import admin
from .models import Blog, Post, PostTag, Tag, Comment, Subscription, Category, Like

# Register your models here.
admin.site.register(Blog)
admin.site.register(Post)
admin.site.register(PostTag)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Subscription)
admin.site.register(Category)
admin.site.register(Like)