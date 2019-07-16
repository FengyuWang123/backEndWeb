from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from public.forms import *
from public.models import *

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