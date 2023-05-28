from django.db import models
from post.models import Post
from django.contrib.auth.models import User

# Create your models here.
class Comment(models.Model):
    id = models.BigAutoField(primary_key=True)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author}: {self.comment}"