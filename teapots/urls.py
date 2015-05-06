from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', include('backend.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url("", include('django_socketio.urls')),
]
