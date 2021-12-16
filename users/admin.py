from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from users.forms import (CustomUserCreationForm,
                         CustomUserChangeForm,
                         )
from users.models import User


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('email', 'first_name', 'last_name', 'number_tel', 'is_staff', 'is_active',)
    list_filter = ('email', 'first_name', 'last_name', 'number_tel', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'first_name', 'last_name', 'number_tel', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(User, CustomUserAdmin)
admin.site.unregister(Group)
