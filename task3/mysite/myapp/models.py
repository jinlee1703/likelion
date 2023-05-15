from django.db import models
from django.contrib.auth.models import User

# Blog 테이블
class Blog(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# Category 테이블
class Category(models.Model):
    category = models.CharField(primary_key=True, unique=True, max_length=20)

    def __str__(self):
        return self.category

# Tag 테이블
class Tag(models.Model):
    tag = models.CharField(primary_key=True, unique=True, max_length=20)

    def __str__(self):
        return self.tag

# Post 테이블
class Post(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)
    blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# Comment 테이블
class Comment(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment

# PostTag 테이블
class PostTag(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE)