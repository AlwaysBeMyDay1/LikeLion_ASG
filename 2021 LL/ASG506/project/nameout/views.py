from django.shortcuts import render

# Create your views here.
def home(request) :
    return render(request, 'home.html')

def outpage(request) :
    userName = request.GET['name']
    return render(request, 'outpage.html', {'userName':userName})