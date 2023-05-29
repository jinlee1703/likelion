from django.urls import path, include
from . import views

urlpatterns = [
    # my_apps
    path('post/create', views.post_create, name='post_create'),
    path('post', views.post_list, name='post_list'),
    path('post/<int:pk>', views.post_detail, name='post_detail'),
    path('post/<int:pk>/update', views.post_update, name='post_update'),
    path('post/<int:pk>/delete', views.post_delete, name='post_delete'),
]