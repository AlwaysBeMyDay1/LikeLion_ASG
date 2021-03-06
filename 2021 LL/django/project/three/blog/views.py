from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from .models import Blog

# Create your views here.
def blog_home(request):
    blogs = Blog.objects.all()
    return render(request, 'blog_home.html', {'blogs' : blogs})

def detail(request, id):
    blog = get_object_or_404(Blog, pk=id)
    return render(request, 'detail.html', {'blog':blog})

def new(request):
    return render(request, 'new.html')

def create(request):
    new_blog = Blog()
    new_blog.title = request.POST['title']
    new_blog.writer = request.POST['writer']
    new_blog.body = request.POST['body']
    new_blog.pub_date = timezone.now()
    new_blog.save()
    return redirect('blog:detail', new_blog.id)

def edit(request, id):
    edit_blog = get_object_or_404(Blog, pk=id)
    return render(request, 'edit.html', {'blog' : edit_blog})

def update(request, id):
    update_blog = get_object_or_404(Blog, pk=id)
    update_blog.title = request.POST['title']
    update_blog.writer = request.POST['writer']
    update_blog.body = request.POST['body']
    update_blog.pub_date = timezone.now()
    update_blog.save()
    return redirect('blog:detail', update_blog.id)

def delete(request, id):
    delete_blog = get_object_or_404(Blog, pk = id)
    delete_blog.delete()
    return redirect('home')