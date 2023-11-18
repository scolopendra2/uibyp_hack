from django.contrib import admin

from . import models

admin.site.register(models.Category)
admin.site.register(models.Question)
admin.site.register(models.Mark)


@admin.register(models.Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = (
        'login',
        'password',
    )
    filter_horizontal = ('categories',)
    fieldsets = (
        (None, {'fields': ('login', 'password')}),
        ('Categories', {'fields': ('categories',)}),
    )

    def get_form(self, request, obj=None, **kwargs):
        self.exclude = (
            'first_name',
            'last_name',
            'email',
            'is_active',
            'is_staff',
            'is_superuser',
            'groups',
            'user_permissions',
            'last_login',
            'date_joined',
            'username',
        )
        return super().get_form(request, obj, **kwargs)
