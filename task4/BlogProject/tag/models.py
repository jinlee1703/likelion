from django.db import models
from blog.models import Blog

# Create your models here.
class Tag(models.Model):
    id = models.BigAutoField(primary_key=True)
    blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE, default='')
    tag = models.CharField(unique=True, max_length=20)

    def __str__(self):
        return self.tag