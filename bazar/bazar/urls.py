"""bazar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework import schemas
from rest_framework_swagger.views import get_swagger_view

from bazar import settings

swagger_view = get_swagger_view(title='bazar')
schema_view= schemas.get_schema_view(title='bazar')
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('api.urls')),
    # url(r'^$', schema_view), url(r'^cart/', include('cart.urls', namespace='cart')),
    # url(r'^cart/', include('api.cart.urls', namespace='cart')),
    # url(r'^', include('api.shop.urls', namespace='shop')),
    url(r'^$', swagger_view),
    url(r'^schema', schema_view),
    # url(r'^media/', include('media')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
