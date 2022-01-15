from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def greeting(request):
    uname1=request.GET['uname']
    context = {'uname':uname1}
    return render(request, 'greeting.html', context)