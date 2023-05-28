from django import forms
from .models import Subscription

class SubscriptionForm(forms.Form):
    class Meta:
        model = Subscription
        fields = ('blog_id', 'user_id')
