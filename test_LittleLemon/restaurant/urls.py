#define URL route for index() view
from django.urls import path, include
from . import views
#from django.contrib import admin
#from rest_framework.authtoken.views import obtain_auth_token



urlpatterns = [

    path('', views.index, name='index'),
    path('menu-items/', views.menuView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    #path('message/', views.msg),
    #path('api-token-auth/', obtain_auth_token),
]
