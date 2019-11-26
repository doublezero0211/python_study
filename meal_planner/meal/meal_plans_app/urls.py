"""定义meal_plans_app的url模式"""
from django.urls import path
from . import views

app_name = 'meal_plans_app'
urlpatterns = [
        #主页
        path('', views.index, name='index'),
]

