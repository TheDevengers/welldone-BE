from django.shortcuts import render


def error_404(request, exception):
        data = {}
        return render(request,'articles/error.html', data)


def error_500(request):
        data = {}
        return render(request,'articles/error.html', data)