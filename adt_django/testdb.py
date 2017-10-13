# -*- coding: utf-8 -*-
#testdb.py


from django.http import HttpResponse

from query.models import Query

def testdb(request):
	#写入数据
	test1=Query(name='zbf32333')
	test1.save()
	return HttpResponse("<p>数据添加成功！</p>");


def get_data(request):
	#初始化
	response=""
	response1=""

	#获取所有数据行，SELECT * FROM
	list =Query.objects.all()

	#filter 相当与where， 设置条件过滤结果
	response2=Query.objects.filter(id=1)

	#获取单个对象
	response3=Query.objects.get(id=1)

	#限制返回的数据
	Query.objects.order_by('name')[0:2]

	#数据排序
	Query.objects.order_by('id')

	#方法可以连锁使用
	Query.objects.filter(name='zbf').order_by('id')

	#输出所有数据：
	for var in list:
		response1+=var.name+" "
	response=response1
	return HttpResponse("<p>"+response+"</p>")