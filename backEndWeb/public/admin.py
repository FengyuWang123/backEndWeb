from django.contrib import admin
from .models import *

class Member1Admin(admin.ModelAdmin):
	list_display = ['id','name']
	list_filter = ['name']
	search_fields = ['name']
	list_per_page = 10
	fields = ['name', 'phone', 'user_id', 'state']


admin.site.register(Member1Model,Member1Admin)
