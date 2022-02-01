import re
from django.shortcuts import get_object_or_404, render, redirect
from .models import Blog
from django.utils import timezone
from .forms import BlogForm, BlogModelForm

def home(req) :
    # posts = Blog.objects.all()
    posts = Blog.objects.filter().order_by("-date")
    return render(req, "index.html", {"posts":posts})

def new(req):
    return render(req, "new.html")

def create(req):
    if(req.method == 'POST'):
        post = Blog()
        post.title = req.POST['title']
        post.body = req.POST['body']
        post.date = timezone.now()
        post.save()
    return redirect('home')

def djangoform(req):
    if req.method=='POST':
        form = BlogForm(req.POST)
        if form.is_valid():
            post = Blog()
            post.title = form.cleaned_data["title"]
            post.body = form.cleaned_data["body"]
            post.save()
            return redirect('home')
    else:
        form = BlogForm()
    return render(req, "djangoform.html",{'form':form})

def modelform(req):
    if req.method=='POST':
        form = BlogModelForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BlogModelForm()
    return render(req, "modelform.html",{'form':form})

def detail(req, blog_id):
    # blog_id 번째 블로그 글을 데이터베이스로부터 가져와서
    blog_detail=get_object_or_404(Blog,pk=blog_id)
    # blog_id 번째 블로그 글을 detail.html로 띄워주는 코드
    return render(req,"detail.html", {'blog_detail':blog_detail})