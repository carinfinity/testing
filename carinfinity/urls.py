from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from myapp import urls

#django hreader customisation
admin.site.site_header = "Car Infinity Admin Portal"
admin.site.site_title = "Welcome to Car Infinity Admin Portal"
admin.site.index_title = "Welcome to the admin portal"

urlpatterns = [
    path('',include('myapp.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)