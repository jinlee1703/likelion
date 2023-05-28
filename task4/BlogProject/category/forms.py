from django import forms
from .models import Category

class CategoryForm(forms.Form):
    class Meta:
        model = Category
        fields = ('blog_id', 'category')
