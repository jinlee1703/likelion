from django import forms
from .models import Like

class LikeForm(forms.Form):
    class Meta:
        model = Like
        fields = ('post_id', 'user_id')
