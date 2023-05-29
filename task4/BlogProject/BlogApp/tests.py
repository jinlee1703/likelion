from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post, Blog, Category


class PostViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.blog = Blog.objects.create(owner=self.user, title='Test Blog')
        self.category = Category.objects.create(title='Test Category')
        self.post = Post.objects.create(blog=self.blog, category=self.category, title='Test Post', body='This is a test post.')

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_post_create_view(self):
        self.client.login(username='testuser', password='testpassword')
        data = {
            'blog_id': self.blog.pk,
            'category_id': self.category.pk,
            'title': 'New Post',
            'body': 'This is a new post.'
        }
        response = self.client.post(reverse('post_create'), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('post_detail', args=[2]))  # Assuming this is the second post created

    def test_post_detail_view(self):
        response = self.client.get(reverse('post_detail', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail.html')

    def test_post_update_view(self):
        self.client.login(username='testuser', password='testpassword')
        data = {
            'blog_id': self.blog.pk,
            'category_id': self.category.pk,
            'title': 'Updated Post',
            'body': 'This is an updated post.'
        }
        response = self.client.post(reverse('post_update', args=[self.post.pk]), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('post_detail', args=[self.post.pk]))

    def test_post_delete_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('post_delete', args=[self.post.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
