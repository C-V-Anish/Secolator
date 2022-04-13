from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def Result(request):
    djtext= request.GET.get('a', 'default')
    djtext1= request.GET.get('ab', 'default')
    c = request.GET.get('abc', 'default')
    try:
        a=int(djtext)
        b=int(djtext1)
        if(c=="+"):
            return HttpResponse(a+b)
        elif(c=="-"):
            return HttpResponse(a-b)
        elif (c == "*"):
            return HttpResponse(a*b)
        elif (c == "/"):
            return HttpResponse(a/b)
        elif (c == "%"):
            return HttpResponse(a%b)
        elif (c == "^"):
            return HttpResponse(a**b)
    except:
        return HttpResponse('Inappropriate datatype...Please enter numbers')