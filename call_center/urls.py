from django.urls import path

from . import views

app_name = 'call_center'

urlpatterns = [
    path('auth/post/', views.auth_check, name='auth_check'),
    path('auth/success/', views.success, name='auth_success'),
]
