from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_fieldsets = (
        (None, {
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
    
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)