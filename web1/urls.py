"""web1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.conf.urls import *
from . import testdb,view,login,forms


urlpatterns = [
	url(r'^testdb$',testdb.testdb),
	url(r'^testdb_a$',testdb.testdb_a),
	url(r'^testdb_b$',testdb.testdb_b),
	url(r'^time$',view.current_datetime),
	url(r'^another_time_page$',view.current_datetime),
	url(r'^time/plus/(\d{1,2})/$',view.hours_ahead),
    path('admin/', admin.site.urls),

	url(r'^index/', login.index),
#   	url(r'^login/', login.login),
    url(r'^login/', view.login),
    url(r'^register/', login.register),
    url(r'^logout/', view.logout),

	url(r'^captcha', include('captcha.urls')),
	url(r'index',view.index),
#	url(r'^confirm/$', views.user_confirm),


]
