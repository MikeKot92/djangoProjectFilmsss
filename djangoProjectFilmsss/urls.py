"""
URL configuration for djangoProjectFilmsss project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from kino import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('kino/', views.kinolist.as_view(), name='allkino'),
    path('kino/otziv/<int:kinoid>/', views.otziv, name='otziv'),
    path('kino/<str:genre>/<slug:pk>/', views.kinoDetail.as_view(), name='onekino'),
    path('actor/', views.actorlist.as_view(), name='allactors'),
    path('actor/<slug:pk>/', views.actorDetail.as_view(), name='oneactor'),
    path('directors/', views.directorlist.as_view(), name='alldirectors'),
    path('directors/<slug:pk>/', views.directorDetail.as_view(), name='onedirector'),  # <slug:pk> - slug конвертор латинских букв и цифр, pk - primary key типа id
    path('auth/', include('django.contrib.auth.urls')),  # include - ссылаемся на пакет в скобочках
    path('auth/registration/', views.register, name = 'register'),
    path('accounts/login/', views.index),
    path('auth/profile', views.profile, name='kabinet'),
    path('auth/profile/change', views.profileChange, name='kabinetChange'),
    path('captcha/', include('captcha.urls')),


]

'''
сброс пароля
reset-password
reset-done
change-password
change-done
home
нужно использовать почтовые сервера для рассылки
'''