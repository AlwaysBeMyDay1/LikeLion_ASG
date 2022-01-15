from django.shortcuts import render

# Create your views here.
def gt_home(request) :
    return render(request, 'gt_home.html')

def gt_result(request) :
    uname1=request.GET['uname']
    context={'uname':uname1}
    return render(request, 'gt_result.html', context)

