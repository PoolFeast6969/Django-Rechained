from django.contrib import admin
admin.AdminSite.site_header = 'Django Rechained'
admin.AdminSite.site_title = 'Django Rechained'
admin.AdminSite.index_title = 'Wow your cool'


from .models import *
class CardAdmin(admin.ModelAdmin):
    list_display = ('content', 'author', 'date_created')


admin.site.register(Answer, CardAdmin)
admin.site.register(Question, CardAdmin)

from django.contrib.auth.admin import UserAdmin
from .models import User

class UserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ('email_valid',)
    fieldsets = None

admin.site.register(User, UserAdmin)
