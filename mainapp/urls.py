
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'mainapp'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('category/list/', views.category_list_view, name='category_list'),
]
