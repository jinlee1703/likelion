from django.db import models
from ..blog.models import Blog
from ..category.models import Category

# Create your models here.
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
