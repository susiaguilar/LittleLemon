#define URL route for index() view
from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [

    path('', views.index, name='index'),
    path('items/', views.menuView.as_view()),
    path('items/<int:pk>', views.SingleMenuItemView.as_view()),
]
