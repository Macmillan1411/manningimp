from django.shortcuts import render,get_object_or_404
from .models import Blog,BlogContent


# Create your views here.
def home(request):
    blog = Blog.objects.get(id = 3)
      # Fetch the related BlogContent objects for the blog
      # Fetch the related BlogContent objects for the blog instance
    blog_content = blog.content.all()
    return render(request,'post.html',{'blog' : blog, 'blog_content' : blog_content})


