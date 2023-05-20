from django.shortcuts import render
from models import Blog

# Create your views here.
def home(request):
    blogs = Blog.objects.filter().order_by('-created_at')

    paginator = Paginator(blogs, 10)    # 최대 10개 표시
    pageNum = request.GET.get('page')   age') # 끊은 객체들을 dict타입으로 저장했다가 pageNumber로써 값을 조회할 수 있게 함
    blogs = paginator.get_page(pageNum)

    return render(request, 'index.html', {'posts': posts})


