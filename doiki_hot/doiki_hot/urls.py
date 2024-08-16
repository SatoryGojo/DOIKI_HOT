from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('porn_site.urls')),
    path('users/', include('registration.urls')),
    path('account/', include('personal_account.urls'))
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


