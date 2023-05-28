from django.db import models
from blog.models import Blog
from django.contrib.auth.models import User

# Create your models here.
class Subscription(models.Model):
    id = models.BigAutoField(primary_key=True)
    blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_id} subscribed to {self.blog_id}"