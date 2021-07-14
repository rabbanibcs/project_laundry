from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from laundry.views import create_invoice
urlpatterns = [
    path('admin/', admin.site.urls),
    path('invoice/<int:id>/',create_invoice,name='invoice'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
