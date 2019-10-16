from django.shortcuts import render


def error_400(request, exception):
        return render(request,'articles/error.html')


def error_403(request, exception):
        return render(request,'articles/error.html')


def error_404(request, exception):
        return render(request,'articles/error.html')


def error_500(request):
        return render(request,'articles/error.html')