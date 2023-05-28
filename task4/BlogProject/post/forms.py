from django import forms
from .models import Post

class PostForm(forms.Form):
    class Meta:
        model = Post
        fields = ('blog_id', 'category_id', 'title', 'body')
