from django.contrib import admin
from django.urls import path, include

from config import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/common/', include('common.urls')),
    path('api/flowers/', include('flowers.urls')),
    path('api/users/', include('user.urls')),
    path('api/address_book/', include('address_book.urls')),
    path('api/reviews/', include('reviews.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

