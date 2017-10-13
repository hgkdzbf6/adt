# -*- coding:utf-8 -*-

from django.conf.urls import *

from . import exam
urlpatterns=[
	url(r'^exam/$',exam.test),
]
