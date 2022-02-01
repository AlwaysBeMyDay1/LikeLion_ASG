import imp
from django import forms
from .models import Blog

class BlogForm(forms.Form):
    title = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)