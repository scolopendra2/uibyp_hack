import json

from django.http import JsonResponse, Http404
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def get_user_text(request):
    if request.method == 'POST':
        # data = json.loads(request.body)
        # user_text = data['text']
        return JsonResponse(
            {'message': 'Данные успешно получены и обработаны.'}
        )
    else:
        raise Http404()


def home(request):
    template = 'homepage/home.html'
    return render(request, template)
