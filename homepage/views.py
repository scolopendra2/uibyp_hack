import json

from django.http import JsonResponse
from django.shortcuts import render

from components.compile_models import text_important, text_category


def home(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_text = data['text']
        task_category = text_category(user_text)
        task_important = text_important(user_text)

        return JsonResponse(
            {'category': task_category, 'task_important': task_important}
        )
    else:
        template = 'homepage/home.html'
        return render(request, template)


def auth(request):
    template = 'homepage/auth.html'
    return render(request, template)
