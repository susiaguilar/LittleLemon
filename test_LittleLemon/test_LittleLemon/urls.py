"""test_LittleLemon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from restaurant import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
#from .views import menuView
#from .views import bookingView 

router = DefaultRouter()
router.register(r'tables', views.BookingViewSet)

#urlpatterns = [
 #   path('admin/', admin.site.urls),
  #  path('restaurant/', include('restaurant.urls')),
   # #path('menu/', menuView.as_view()),
    ##path('booking/', bookingview.as_view()),
    #path('', include(router.urls)),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
  #  path('api/', include('restaurant.urls')),
   # path('restaurant/menu/',include('restaurant.urls')),
 #   path('restaurant/booking/', include(router.urls)),
#]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurant/', include('restaurant.urls')),
    path('restaurant/menu/',include('restaurant.urls')),
    path('restaurant/booking/', include(router.urls)),
    #path('auth/', include('djoser.urls')),
    #path('auth/', include('djoser.urls.authtoken')),
    path('api-token-auth/', obtain_auth_token),
    #path('api/', include('restaurant.urls')),

]

#router = routers.DefaultRouter()
#router.register(r'user', views.UserViewSet)
