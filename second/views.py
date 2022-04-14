from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def Result(request):
    djtext = request.GET.get('a', 'default')
    djtext1 = request.GET.get('ab', 'default')
    c = request.GET.get('abc', 'default')
    try:
        a = int(djtext)
        b = int(djtext1)
        if (c == "+"):
            x = {'Purpose': 'Addition', 'Result': a + b}
            return render(request, 'Result.html', x)
        elif (c == "-"):
            x = {'Purpose': 'Subtraction','Result': a - b}
            return render(request, 'Result.html', x)
        elif (c == "*"):
            x = {'Purpose': 'Multiplication', 'Result': a * b}
            return render(request, 'Result.html', x)
        elif (c == "/"):
            x = {'Purpose': 'Division', 'Result': a / b}
            return render(request, 'Result.html', x)
        elif (c == "%"):
            x = {'Purpose': 'Remainder', 'Result': a % b}
            return render(request, 'Result.html', x)
        elif (c == "^"):
            x = {'Purpose': 'Power', 'Result': a ** b}
            return render(request, 'Result.html', x)
        else :
            return HttpResponse("Enter appropriate operator")
    except:
        return HttpResponse('Inappropriate datatype....Please enter carefully')
