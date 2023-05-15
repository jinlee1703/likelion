from django.contrib import admin
from .models import Blog, Category, Tag, Post, Comment, PostTag

# Register your models here.
admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(PostTag)