from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class MyUserAdmin(UserAdmin):
    list_display = ('email', 'email_valid')

admin.site.register(User, MyUserAdmin)
