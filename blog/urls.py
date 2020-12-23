"""Bproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('wr/', views.write, name='wr'),
    path('wrCon/', views.wrCon, name='wrCon'),
    path('main/', views.main, name='main'),
    path('main/<str:title>/view/', views.viewDet, name='view'),
    path('main/<str:title>/mod/', views.modDet, name='modify'),
    path('main/<str:title>/del/', views.delPost, name='delete'),
]
