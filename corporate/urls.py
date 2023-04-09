from django.urls import path, include
from . import views

urlpatterns = [
    path('list', views.PersonaldetailsFields.as_view(), name='list'),
]
