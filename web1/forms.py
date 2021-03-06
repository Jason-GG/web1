# -*- coding: UTF-8 -*-

from django import forms
from captcha.fields import CaptchaField
from TestModel import models

class UserForm(forms.Form):
	username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
	password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
#	captcha = CaptchaField(label='验证码')


#数据库支撑页面设置
#class UserForm(forms.ModelForm):
#    class Meta:
#        model = models.User
#        fields = ['name', 'password']
#
#    def __init__(self, *args, **kwargs):
#        super(UserForm, self).__init__(*args, *kwargs)
#        self.fields['name'].label = '用户名'
#        self.fields['password'].label = '密码'
