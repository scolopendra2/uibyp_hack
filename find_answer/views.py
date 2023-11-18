import json
from .find import get_res
from .models import Questions
from django.http import JsonResponse, Http404, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from .compile_models import text_important, text_category


@csrf_exempt
def get_questions(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_text = data['text']
            count = data['count']
            questions = Questions.objects.all()
            return JsonResponse(
                {'questions': f'{get_res(user_text, count, questions)}'}
            )
        except json.decoder.JSONDecodeError:
            return HttpResponseBadRequest('Invalid JSON data')
    else:
        raise Http404()


@csrf_exempt
def get_answer(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            questions_text = data['questions']
            questions = Questions.objects.get(question=questions_text)
            return JsonResponse({'answer': questions.answer})
        except json.decoder.JSONDecodeError:
            return HttpResponseBadRequest('Invalid JSON data')
    else:
        raise Http404()


@csrf_exempt
def add_task_to_moder(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_text = data['text']
            task_category = text_category(user_text)
            task_important = text_important(user_text)
            # Это надо заменить на запрос к
            # БД который будет искать чела
            # с {task_category} и давать ему таск
            return JsonResponse(
                {'category': task_category, 'task_important': task_important}
            )
        except json.decoder.JSONDecodeError:
            return HttpResponseBadRequest('Invalid JSON data')
    else:
        raise Http404()
