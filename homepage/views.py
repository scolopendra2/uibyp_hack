import json

from django.shortcuts import render, redirect

from call_center.models import Question, Category
from components.compile_models import text_important, text_category
from . import models


def home(request):
    template = 'homepage/home.html'
    user_session_id = request.session.get('user_session_id', None)
    questions = Question.objects.filter(id_user=user_session_id).all()
    context = {
        'questions': questions,
    }
    return render(request, template, context)


def post_question(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_text = data['text']
        task_category = text_category(user_text)
        task_important = text_important(user_text)
        user_session_id = request.session.get('user_session_id', None)
        if not user_session_id:
            user = models.User()
            request.session['user_session_id'] = user.user_id
            user_session_id = user.user_id
            user.save()
        category_id = Category.objects.get(name=task_category)

        question = Question()
        question.question = user_text
        question.id_category = category_id
        question.id_user = user_session_id
        question.id_worker = question.get_id_for_question(task_category)
        question.important = task_important
        question.save()
        return redirect('/')


def auth(request):
    template = 'homepage/auth.html'
    return render(request, template)
