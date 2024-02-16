from django.contrib import admin
from django.urls import path, include
from .views import *
from .import views

urlpatterns = [
    path('', index, name='index'),
    path('add', views.add, name = 'add'),
    path('update/<int:todo_id>/', views.update, name = 'update'),
    path('delete/<int:todo_id>/', views.delete, name = 'delete'),

]
