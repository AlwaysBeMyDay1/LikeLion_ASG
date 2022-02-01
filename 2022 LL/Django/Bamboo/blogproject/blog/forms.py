import imp
from django import forms
from .models import Blog

class BlogForm(forms.Form):
    title = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)

class BlogModelForm(forms.ModelForm):
    class Meta:
        model = Blog
        # fields = '__all__' #<---- 모든 필드 
        fields = ['title','body']
