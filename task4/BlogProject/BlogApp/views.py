from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .forms import PostForm
from .models import Post, Blog, Category
import json


def home(request):
    # posts = Post.objects.all()
    posts = Post.objects.filter().order_by('-create_dt')

    paginator = Paginator(posts, 5)  # 객체, 끊어내는 개수
    pageNum = request.GET.get('page')  # 끊은 객체들을 dict타입으로 저장했다가 pageNumber로써 값을 조회할 수 있게 함
    posts = paginator.get_page(pageNum)

    return render(request, 'index.html', {'posts': posts})


def post_create(request):
    if request.method == 'POST':
        json_data = request.body.decode('utf-8')
        data = json.loads(json_data)

        form = PostForm(data)
        if form.is_valid():
            post = form.save(commit=False)
            post.blog_id = Blog.objects.get(pk=data["blog_id"])
            post.category_id = Category.objects.get(pk=data["category_id"])
            post.title = data["title"]
            post.body = data["body"]
            post.save()
            return HttpResponseRedirect(reverse('post_detail', args=[post.pk]))
        else:
            print(form.errors.as_text())
            return HttpResponse('Invalid form data')
    else:
        form = PostForm()
        return render(request, 'post_form.html', {'form': form})


def post_list(request):
    posts = Post.postobjects.all()
    print(f" post_list : {posts} ")
    return HttpResponse('Post list.')


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    print(f" post_detail : {post} ")
    return HttpResponse('Post detail.')


def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user.blog
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return HttpResponse('Post update.')


def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    # messages.success(request, "Post deleted successfully.")
    return redirect('home')
