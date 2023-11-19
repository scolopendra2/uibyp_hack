import json

from django.http import HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

from homepage.models import User
from . import models


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
        categories = [category.name for category in worker.categories.all()]
        questions_no_answer = models.Question.objects.filter(id_worker=worker.id,
                                                             status=False).all()

        questions_yes_answer = models.Question.objects.filter(id_worker=worker.id,
                                                              status=True).all()
        context = {
            'exit': True,
            'categories': ', '.join(categories),
            'name': worker.login,
            'questions_no_answer': questions_no_answer,
            'questions_yes_answer': questions_yes_answer
        }
        return render(request, template, context=context)
    else:
        error_message = 'Неверный логин или пароль'
        return render(
            request, 'homepage/auth.html', {'error_message': error_message}
        )


def answer_post(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        answer = data['answer']
        id_question = int(data['id'].split(':')[1])
        question = models.Question.objects.filter(id=id_question).first()
        question.answer = answer
        question.status = True
        question.save()
        return redirect('call_center:auth_success')
