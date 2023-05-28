from django import forms
from .models import Comment

class CommentForm(forms.Form):
    class Meta:
        model = Comment
        fields = ('post_id', 'author', 'comment')
