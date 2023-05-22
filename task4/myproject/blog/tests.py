from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
import time
from .models import *

# Create your tests here.
class PostViewTest(TestCase):
    def setUp(self): # user, blog, post, category 더미 데이터 생성
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword',
        )
        self.blog = Blog.objects.create(
            title='Test Blog',
            body='This is a test blog.',
            owner=self.user
        )
        self.post = Post.objects.create(
            title='Test Post',
            excerpt='This is a test post.',
            content='Lorem ipsum dolor sit amet.',
            slug='test-post',
            published='2022-01-01 00:00:00',
            status='published',
            author=self.blog  # 생성한 Blog 객체를 author 필드에 지정
        )
        # 유효한 category_id 값을 가지는 Category 인스턴스 생성
        self.category = Category.objects.create(
            name='Test Category',
            description='This is a test category.'
        ) 

    def test_post_list_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)

    def test_post_detail_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('post_detail', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)

    def test_post_create_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('post_create'))
        self.assertEqual(response.status_code, 302)

        data = {
            'title': 'New Post',
            'excerpt': 'This is a new post.',
            'content': 'Lorem ipsum dolor sit amet.',
            'slug': 'new-post',
            'published': '2022-02-01 00:00:00',
            'status': 'published'
        }
        response = self.client.post(reverse('post_create'), data)
        print(f"response : {response}")
        self.assertEqual(response.status_code, 302)

        time.sleep(1)  # 1초 딜레이 (DB에 저장되는 시간을 기다림)

        self.assertEqual(Post.objects.count(), 2)
        self.assertEqual(Post.objects.get(post_id=2).title, 'New Post')

    def test_post_update_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('post_update', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)

        data = {
            'title': 'Updated Post',
            'excerpt': 'This is an updated post.',
            'content': 'Lorem ipsum dolor sit amet.',
            'slug': 'updated-post',
            'published': '2022-03-01 00:00:00',
            'status': 'published'
        }
        response = self.client.post(reverse('post_update', args=[self.post.pk]), data)
        self.assertEqual(response.status_code, 302)
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, 'Updated Post')

    def test_post_delete_view(self):
        response = self.client.get(reverse('post_delete', args=[self.post.pk]))
        self.assertEqual(response.status_code, 302)

        self.post = Post.objects.create(
            title='Test Post',
            excerpt='This is a test post.',
            content='Lorem ipsum dolor sit amet.',
            slug='test-post',
            published='2022-01-01 00:00:00',
            status='published',
            author=self.blog 
        )
        response = self.client.post(reverse('post_delete', args=[self.post.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.count(), 0)