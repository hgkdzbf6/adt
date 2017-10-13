"""adt_django URL Configuration

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
from django.conf.urls import url, include 
from django.contrib import admin
from query import views as vv
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	url(r'^admin/',admin.site.urls),
    url(r'^query/$', vv.hello),
    url(r'^query/$', vv.querying,name="query"),
    url(r'^index/$',vv.index),
    url(r'^cost/$',vv.cost),
    url(r'^black/$',vv.black),
    url(r'^insertWords/$',vv.insertWords),
    url(r'^blog/',include('index.urls')),
    url(r'^show/$',vv.show),
    url(r'^upload/$',vv.upload),
    url(r'^success/$',vv.success),
    url(r'^register/$',vv.register),
    url(r'^login/$',vv.login),
    url(r'^logout/$',vv.logout),
    url(r'^error/$',vv.error),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
