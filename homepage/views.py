from django.shortcuts import render


def home(request):
    template = 'homepage/home.html'
    return render(request, template)


def auth(request):
    template = 'homepage/auth.html'
    return render(request, template)
