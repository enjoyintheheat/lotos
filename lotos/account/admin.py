from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .forms import (
    UserChangeForm, UserCreationForm
)
from .models import User

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ['email', 'is_staff']
    list_filter = ('is_staff',)
    fieldsets = (
        (None, {
            'fields': ('email', 'password')
        }),
        ('Персонал', {
            'fields': ('is_staff', 'is_superuser')
        }),
        ('Права', {
            'fields': ('user_permissions',)
        }),
        ('Группы', {
            'fields': ('groups',)
        })
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
        ('Права', {
            'fields': ('user_permissions',)
        }),
        ('Группы', {
            'fields': ('groups',)
        })
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(User, UserAdmin)
