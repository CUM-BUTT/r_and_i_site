from django.contrib import admin
from django.urls import path
from ridt_site import views

urlpatterns = [
    path('', views.Home.as_view()),
    path('home/', views.Home.as_view()),
    path('url_input/', views.GoToBuilder.as_view()),
    path('build/', views.GoToSuccess.as_view())
]