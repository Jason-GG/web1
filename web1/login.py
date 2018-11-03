# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.shortcuts import redirect

def index(request):
	pass
	return render(request,'login/index.html')

def login(request):
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		message = "所有空都必须填满!!!"
		if username and password: 
			username = username.strip()
			try:
				user = models.User.objects.get(name=username)
				if user.password == password:
					return redirect('/index/')
				else:
					message = "密码不正确!!!"
			except:
				message = "用户名不存在!!!"
			return render(request,'login/login.html',{"message":message})
		print (username,password)
		return redirect('/index/')
	return render(request,'login/login.html')

def register(request):
	pass
#    if request.session.get('is_login', None):
#        # 登录状态不允许注册。你可以修改这条原则！
#        return redirect("/index/")
#    if request.method == "POST":
#        register_form = forms.RegisterForm(request.POST)
#        message = "请检查填写的内容！"
#        if register_form.is_valid():  # 获取数据
#            username = register_form.cleaned_data['username']
#            password1 = register_form.cleaned_data['password1']
#            password2 = register_form.cleaned_data['password2']
#            email = register_form.cleaned_data['email']
#            sex = register_form.cleaned_data['sex']
#            if password1 != password2:  # 判断两次密码是否相同
#                message = "两次输入的密码不同！"
#                return render(request, 'login/register.html', locals())
#            else:
#                same_name_user = models.User.objects.filter(name=username)
#                if same_name_user:  # 用户名唯一
#                    message = '用户已经存在，请重新选择用户名！'
#                    return render(request, 'login/register.html', locals())
#                same_email_user = models.User.objects.filter(email=email)
#                if same_email_user:  # 邮箱地址唯一
#                    message = '该邮箱地址已被注册，请使用别的邮箱！'
#                    return render(request, 'login/register.html', locals())
#
#                # 当一切都OK的情况下，创建新用户
#
#                new_user = models.User()
#                new_user.name = username
#                new_user.password = hash_code(password1)  # 使用加密密码
#                new_user.email = email
#                new_user.sex = sex
#                new_user.save()
#
#                code = make_confirm_string(new_user)
#                send_email(email, code)
#
#                message = '请前往注册邮箱，进行邮件确认！'
#                return render(request, 'login/confirm.html', locals())  # 跳转到等待邮件确认页面。
#
#    register_form = forms.RegisterForm()
#
	return render(request,'login/register.html')

def logout(request):
	pass
	return redirect("/index/")

def make_confirm_string(user):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    code = hash_code(user.name, now)
    models.ConfirmString.objects.create(code=code, user=user,)
    return code


def send_email(email, code):

    from django.core.mail import EmailMultiAlternatives

    subject = ''

    text_content = ''' ... '''

    html_content = '''
                    '''.format('127.0.0.1:8000', code, settings.CONFIRM_DAYS)

#    msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [email])
#    msg.attach_alternative(html_content, "text/html")
#    msg.send()
