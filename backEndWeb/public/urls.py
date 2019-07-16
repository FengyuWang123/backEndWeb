
from django.urls import path, re_path
from django.views.generic.base import TemplateView

from . import views

app_name = 'public'

urlpatterns = [
	path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('charts', views.charts, name='charts'),
    path('elements', views.elements, name='elements'),
    path('icons', views.icons, name='icons'),
    path('notifications', views.notifications, name='notifications'),
    path('page-lockscreen', views.pageLockscreen, name='page-lockscreen'),
    path('page-login', views.pageLogin, name='page-login'),
    path('page-profile', views.pageProfile, name='page-profile'),
    path('panels', views.panels, name='panels'),
    path('tables', views.tables, name='tables'),
    path('typography', views.typography, name='typography'),

]