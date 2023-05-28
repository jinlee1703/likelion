from django.urls import path
from .views import BlogView

urlpatterns = [
    path('create/', BlogView.create)
]