from django import forms
from .models import PostTag

class PostTagForm(forms.Form):
    class Meta:
        model = PostTag
        fields = ('post_id', 'tag_id')
