from django.conf import settings
from django.contrib import admin
from django.urls import include, path

app_name = 'chat_road'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('bot/', include('find_answer.urls')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)
