from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from django.core import serializers


from public.forms import *
from public.models import *
from public.helper import *

import json

# templates
def index(request):
	context = {}
	return render(request, '../templates/index.html', context)

def charts(request):
	context = {}
	return render(request, '../templates/charts.html', context)

def elements(request):
	context = {}
	return render(request, '../templates/elements.html', context)

def icons(request):
	context = {}
	return render(request, '../templates/icons.html', context)

def notifications(request):
	context = {}
	return render(request, '../templates/notifications.html', context)

def pageLockscreen(request):
	context = {}
	return render(request, '../templates/page-lockscreen.html', context)

def pageLogin(request):
	context = {}
	return render(request, '../templates/page-login.html', context)

def pageProfile(request):
	context = {}
	return render(request, '../templates/page-profile.html', context)

def panels(request):
	context = {}
	return render(request, '../templates/panels.html', context)

def tables(request):
	context = {}
	return render(request, '../templates/tables.html', context)

def typography(request):
	context = {}
	return render(request, '../templates/typography.html', context)

# work on
def mainPage(request):
	context = {}
	return render(request, '../templates/mainPage.html', context)

def member1(request):
	context = {}
	# sql = """select * from member1model"""
	# member1_data = RunSQL(sql)
	member1_data = Member1Model.objects.all()
	# 将数据按照规定每页显示 10 条, 进行分割
	paginator = Paginator(member1_data, 10)
	
	if request.method == "GET":
		# 获取 url 后面的 page 参数的值, 首页不显示 page 参数, 默认值是 1
		page = request.GET.get('page')
		try:
			members = paginator.page(page)
		# todo: 注意捕获异常
		except PageNotAnInteger:
			# 如果请求的页数不是整数, 返回第一页。
			members = paginator.page(1)
		except InvalidPage:
			# 如果请求的页数不存在, 重定向页面
			return HttpResponse('找不到页面的内容')
		except EmptyPage:
			# 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
			members = paginator.page(paginator.num_pages)
	
	return render(request, '../templates/member1.html', {'members': members,'member1data':member1_data})

def member2(request):
	context = {}
	# sql = """select * from member1model"""
	# member1_data = RunSQL(sql)
	member1_data = Member1Model.objects.all()
	# 将数据按照规定每页显示 10 条, 进行分割
	paginator = Paginator(member1_data, 10)
	
	if request.method == "GET":
		# 获取 url 后面的 page 参数的值, 首页不显示 page 参数, 默认值是 1
		page = request.GET.get('page')
		try:
			members = paginator.page(page)
		# todo: 注意捕获异常
		except PageNotAnInteger:
			# 如果请求的页数不是整数, 返回第一页。
			members = paginator.page(1)
		except InvalidPage:
			# 如果请求的页数不存在, 重定向页面
			return HttpResponse('找不到页面的内容')
		except EmptyPage:
			# 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
			members = paginator.page(paginator.num_pages)
	
	return render(request, '../templates/member2.html', {'members': members,'member1data':member1_data})

def member3(request):
	# sql = """select * from member1model"""
	# member1_data = RunSQL(sql)
	member1_data = Member1Model.objects.all()
	# # 将数据按照规定每页显示 10 条, 进行分割
	# paginator = Paginator(member1_data, 10)
	
	data = {}
	data['list'] = json.loads(serializers.serialize("json", member1_data))
	print(data)
	
	return render(request, '../templates/member3.html', {'member1data':data})

def equipManage(request):
	context = {}
	return render(request, '../templates/equipManage.html', context)

def systemManage(request):
	context = {}
	return render(request, '../templates/systemManage.html', context)

