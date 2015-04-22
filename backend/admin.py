from django.contrib import admin
admin.AdminSite.site_header = 'Django Rechained'
admin.AdminSite.site_title = 'Django Rechained'
admin.AdminSite.index_title = 'Wow your cool'

from .models import *

class CardAdmin(admin.ModelAdmin):
    list_display = ('content', 'author', 'votes', 'uses', 'date_created')

admin.site.register(Answer, CardAdmin)
admin.site.register(Question, CardAdmin)

from django.contrib.auth.admin import UserAdmin
from .models import User

class UserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ('email_valid',)
    fieldsets = (
            (None, {
                'fields': ('username', 'password')
            }),
            ('Personal Info', {
                'fields': ('first_name', 'last_name', ('email', 'email_valid'))
            }),
            ('Permissions', {
                'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
            }),
            ('Important Dates', {
                'fields': ('last_login', 'date_joined')
            }),
    )

admin.site.register(User, UserAdmin)
