from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def Result(request):
    djtext = request.GET.get('abc', 'default')
    c: int=0
    for char in djtext:
        c=c+1
    params = {'purpose': 'Character Count', 'analysed_text': c}
    return render(request,'Result.html',params)

