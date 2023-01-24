from django.contrib import admin
from django.urls import path  , include
from django.conf.urls.static import static
from . import settings

admin.site.site_header = "Sun-Shine Admin"
admin.site.site_title = "Catering manager Admin Portal"
admin.site.index_title = "Welcome to Sun-Shine Catering Serices"

urlpatterns = [
    path('dashboard', admin.site.urls),
    path('' , include('store.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
