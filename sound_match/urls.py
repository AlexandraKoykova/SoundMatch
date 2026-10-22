
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path(
        '',
        TemplateView.as_view(template_name='home.html'),
        name='home'
    ),
    path('admin/', admin.site.urls),
    path('artists/', include('artists.urls')),
    path('bookings/', include('bookings.urls')),
    path('genres/', include('genres.urls')),
    path('reviews/', include('reviews.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )