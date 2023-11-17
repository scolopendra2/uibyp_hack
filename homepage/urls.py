from django.urls import path

from . import views

app_name = 'homepage'

urlpatterns = [
    path('get_text/', views.get_user_text, name='get_text'),
]
