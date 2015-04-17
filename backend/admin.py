from django.contrib import admin
admin.AdminSite.site_header = 'Django Rechained'
admin.AdminSite.site_title = 'Django Rechained'
admin.AdminSite.index_title = 'Wow your cool'


from .models import Card
class CardAdmin(admin.ModelAdmin):
    list_display = ('content', 'type', 'author', 'date_created')
    list_filter = ['type']


admin.site.register(Card, CardAdmin)
