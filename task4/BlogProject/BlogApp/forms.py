from django import forms
from .models import Blog, Post, PostTag, Tag, Comment, Subscription, Category, Like


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('owner', 'title', 'description')


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('blog_id', 'category')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('post_id', 'author', 'comment')


class LikeForm(forms.ModelForm):
    class Meta:
        model = Like
        fields = ('post_id', 'user_id')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('blog_id', 'category_id', 'title', 'body')


class PostTagForm(forms.ModelForm):
    class Meta:
        model = PostTag
        fields = ('post_id', 'tag_id')


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ('blog_id', 'user_id')


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('blog_id', 'tag')
