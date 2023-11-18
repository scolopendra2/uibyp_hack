from django.urls import path

from . import views

app_name = 'answer'

urlpatterns = [
    path('questions/', views.get_questions, name='get_questions'),
    path('answer/', views.get_answer, name='get_answer'),
    path('add/', views.add_task_to_moder, name='add_task'),
]
