
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from employee import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('employee.urls')),


]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

