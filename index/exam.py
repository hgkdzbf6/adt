# -*- coding: utf-8 -*-
#exam.py
from django.http import HttpResponse

from index.models import Index

def test(request):
	test1=Index(name='zbf')
	test1.save()
	return HttpResponse('<p>数据添加成功</p>')