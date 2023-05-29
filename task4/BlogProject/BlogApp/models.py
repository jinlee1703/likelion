from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Blog(models.Model):
    id = models.BigAutoField(primary_key=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}: {self.description}"


class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE)
    category = models.CharField(unique=True, max_length=20)

    def __str__(self):
        return self.category


class Like(models.Model):
    id = models.BigAutoField(primary_key=True)
    post_id = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_id} likes {self.post_id}"


class Post(models.Model):
    id = models.BigAutoField(primary_key=True)
    blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    view_cnt = models.PositiveIntegerField(default=0)
    is_hidden = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}: {self.body}"


class Comment(models.Model):
    id = models.BigAutoField(primary_key=True)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author}: {self.comment}"


class Tag(models.Model):
    id = models.BigAutoField(primary_key=True)
    blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE)
    tag = models.CharField(unique=True, max_length=20)

    def __str__(self):
        return self.tag


class PostTag(models.Model):
    id = models.BigAutoField(primary_key=True)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return f"Post: {self.post} | Tag: {self.tag}"


class Subscription(models.Model):
    id = models.BigAutoField(primary_key=True)
    blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_id} subscribed to {self.blog_id}"
