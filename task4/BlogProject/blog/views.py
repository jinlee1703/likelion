from django.http import HttpResponse
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Blog
from .forms import BlogForm

# Create your models here.
class BlogView(APIView):
    permission_classes = [AllowAny]

    @staticmethod
    def create(request):
        print(request.POST)
        # if request.method == 'POST':
        #     form = BlogForm(request.POST)
        #     if form.is_valid():
        #         blog = form.save(commit=False)
        #         blog.owner = request.POST["owner"]
        #         blog.title = request.POST["title"]
        #         blog.description = request.POST["description"]
        #         blog.save()
        #         return HttpResponse("Blog Create Success!!", status=status.HTTP_201_CREATED)
        # else:
        #     form = BlogForm()
        return HttpResponse("Blog Create Failed!!", status=status.HTTP_400_BAD_REQUEST)
