from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from fake_generator import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('schemas_structure.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
                                                                           document_root=settings.STATIC_ROOT)
