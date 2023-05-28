from django.db import models
from ..post.models import Post
from ..tag.models import Tag

# Create your models here.
class PostTag(models.Model):
    id = models.BigAutoField(primary_key=True)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return f"Post: {self.post} | Tag: {self.tag}"