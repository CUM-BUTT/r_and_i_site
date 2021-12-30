from django.contrib import admin
from django.urls import path
from ridt_site import views

urlpatterns = [
    path('', views.Home),
    path('home/', views.Home),
    path('url_input/', views.GoToBuilder),
    path('build/', views.Builder)
]