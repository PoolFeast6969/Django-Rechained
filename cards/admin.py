from django.contrib import admin
from .models import *

class CardAdmin(admin.ModelAdmin):
    list_display = ('content', 'author', 'votes', 'uses', 'date_created')

admin.site.register(Answer, CardAdmin)
admin.site.register(Question, CardAdmin)
