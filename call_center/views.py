from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

from . import models
from homepage.models import User


@csrf_protect
def auth_check(request):
    template = 'homepage/auth.html'

    if request.method == 'POST':
        username = request.POST.get('input_login')
        password = request.POST.get('input_password')
        worker = models.Worker.objects.filter(
            login=username, password=password
        ).first()
        user_session_id = request.session.get('user_session_id', None)
        if not user_session_id:
            user = User()
            request.session['user_session_id'] = user.user_id
            user_session_id = user.user_id
            user.save()
        user = User.objects.filter(user_id=user_session_id).first()
        user.this_worker = True
        user.worker_login = username
        user.worker_password = password
        user.save()
        if worker is not None:
            return redirect('/auth/success')
        else:
            error_message = 'Неверный логин или пароль'
            return render(request, template, {'error_message': error_message})
    else:
        return HttpResponseNotFound()


def success(request):
    user_session_id = request.session.get('user_session_id', None)
    user = User.objects.filter(user_id=user_session_id).first()
    if user is not None and user.this_worker:
        template = 'call_center/worker_card.html'
        login, password = user.worker_login, user.worker_password
        worker = models.Worker.objects.filter(
            login=login, password=password
        ).first()
        context = {
            'exit': True,
            'worker': worker
        }
        return render(request, template, context=context)
    else:
        error_message = 'Неверный логин или пароль'
        return render(
            request, 'homepage/auth.html', {'error_message': error_message}
        )
