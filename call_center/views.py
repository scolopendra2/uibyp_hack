from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

from . import models


@csrf_protect
def auth_check(request):
    template = 'homepage/auth.html'

    if request.method == 'POST':
        username = request.POST.get('input_login')
        password = request.POST.get('input_password')
        user = models.Worker.objects.filter(
            login=username, password=password
        ).first()

        if user is not None:
            return render(request, 'call_center/worker_card.html')
        else:
            error_message = 'Неверный логин или пароль'
            return render(request, template, {'error_message': error_message})
    else:
        return HttpResponseNotFound()
