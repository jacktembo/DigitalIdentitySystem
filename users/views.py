from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, ListCreateAPIView, \
    CreateAPIView, UpdateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView, \
    RetrieveDestroyAPIView, RetrieveUpdateAPIView
from .models import *
from .serializers import *


class UserDetailsView(ListCreateAPIView):
    """
    This View is responsible for listing and creating user profiles.
    """
    def get_queryset(self):
        return get_list_or_404(UserDetails)

    def get_serializer_class(self):
        return UserDetailsSerializer


class UserDetailsDetail(RetrieveUpdateDestroyAPIView):

    def get_queryset(self):
        return UserDetails.objects.all()

    def get_serializer_class(self):
        return UserDetailsSerializer
    # lookup_field = 'pk'

