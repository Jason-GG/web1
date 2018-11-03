# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render

import datetime
from . import forms

from TestModel import models

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def hours_ahead(request,offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
	return HttpResponse(html)

#def login(request):
#    if request.session.get('is_login',None):
#        return redirect("/index/")
#    if request.method == "POST":
#        login_form = forms.UserForm(request.POST)
#        message = "请检查填写的内容！"
#        if login_form.is_valid():
#            username = login_form.cleaned_data['username']
#            password = login_form.cleaned_data['password']
#            try:
#                user = models.User.objects.get(name=username)
#                if user.password == password:
#                    request.session['is_login'] = True
#                    request.session['user_id'] = user.id
#                    request.session['user_name'] = user.name
#                    return redirect('/index/')
#                else:
#                    message = "密码不正确！"
#            except:
#                message = "用户不存在！" 
#    return render(request, 'login/login.html', locals())

def login(request):
    if request.method == "POST":
        login_form = forms.UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.User.objects.get(name=username)
                if user.password == password:
                    return redirect('/index/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在！"
        return render(request, 'login/login.html', locals())

    login_form = forms.UserForm()
    return render(request, 'login/login.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/index/")
    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect("/index/")

#def user_confirm(request):
#    code = request.GET.get('code', None)
#    message = ''
#    try:
#        confirm = models.ConfirmString.objects.get(code=code)
#    except:
#        message = '无效的确认请求!'
#        return render(request, 'login/confirm.html', locals())
#
#    c_time = confirm.c_time
#    now = datetime.datetime.now()
#    if now > c_time + datetime.timedelta(settings.CONFIRM_DAYS):
#        confirm.user.delete()
#        message = '您的邮件已经过期！请重新注册!'
#        return render(request, 'login/confirm.html', locals())
#    else:
#        confirm.user.has_confirmed = True
#        confirm.user.save()
#        confirm.delete()
#        message = '感谢确认，请使用账户登录！'
#        return render(request, 'login/confirm.html', locals())


