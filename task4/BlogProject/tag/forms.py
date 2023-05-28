from django import forms
from .models import Tag

class TagForm(forms.Form):
    class Meta:
        model = Tag
        fields = ('blog_id', 'tag')
