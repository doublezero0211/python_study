"""定义users的url模式"""
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'users'
urlpatterns = [
        # 登录页面
        path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
        # 注销页面
        path('logout', views.logout_view, name='logout'),
        # 注册页面
        path('register', views.register, name='register'),

]

