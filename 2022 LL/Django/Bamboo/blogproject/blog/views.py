import re
from django.shortcuts import render, redirect
from .models import Blog
from django.utils import timezone


def home(req) :
    return render(req, "index.html")

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
    return redirect('home')

def modelform(req):
    return redirect('home')