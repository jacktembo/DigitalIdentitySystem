from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('user-details/', views.UserDetailsView.as_view()),
    path('user-details/<pk>/', views.UserDetailsDetail.as_view()),
]
