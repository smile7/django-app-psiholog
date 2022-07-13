"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from core import views as contact_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include('core.urls')),
    path('summernote/', include('django_summernote.urls')),
    # path('contact/', contact_views.contact_view, name='contact'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# customizing admin interface
admin.site.site_header = 'Petya Dimova Website'
admin.site.site_title = 'Petya Dimova Admin'
admin.site.index_title = 'Petya Administration Panel'
