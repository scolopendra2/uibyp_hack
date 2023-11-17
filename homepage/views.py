import json

from django.http import JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def get_user_text(request):
    print(request.method)
    if request.method == 'POST':
        data = json.loads(request.body)
        user_text = data['text']
        print(user_text)
        return JsonResponse(
            {'message': 'Данные успешно получены и обработаны.'}
        )
    else:
        raise Http404()
