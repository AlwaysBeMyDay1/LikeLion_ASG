from django.shortcuts import render

# Create your views here.
def wc_home(request) :
    return render(request, 'wc_home.html')

def wc_result(request) :
    text=request.GET['text']
    words = text.split()
    wordlist = {
    }
    for word in words:
        if word in wordlist:
            wordlist[word]+=1
        else :
            wordlist[word] = 1
    num = len(wordlist)
    context = {'text':text, 'num':num, 'wordlist':wordlist.items()}
    return render(request, 'wc_result.html', context)