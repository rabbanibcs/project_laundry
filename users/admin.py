from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.conf import settings
from .models import User


class CustomUserAdmin(UserAdmin):
    model = settings.AUTH_USER_MODEL
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name', 'phone')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'email', 'phone', 'password1', 'password2'),
        }),
    )
    list_display_links = ('name', 'email',)
    list_display = ('name', 'email', 'phone', 'last_login', 'is_staff')
    search_fields = ('name', 'email', 'phone')
    ordering = ('name',)


admin.site.register(User, CustomUserAdmin)
