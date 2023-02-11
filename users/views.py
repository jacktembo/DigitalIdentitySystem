from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, ListCreateAPIView, \
    CreateAPIView, UpdateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView, \
    RetrieveDestroyAPIView, RetrieveUpdateAPIView
from .models import *
from rest_framework import viewsets
from .serializers import *


class UserDetailsViewSet(viewsets.ModelViewSet):
    """
    This Router is responsible for creating, reading, updating, and deleting
    UserDetails objects.
    You can get a specific user using the 'national_id_number' lookup field.
    """
    queryset = UserDetails.objects.all()

    serializer_class = UserDetailsSerializer

    lookup_field = 'national_id_number'


class UserDocumentViewSet(viewsets.ModelViewSet):
    queryset = UserDocuments.objects.all()
    serializer_class = UserDocumentSerializer


class BiometricsViewSet(viewsets.ModelViewSet):
    """
    The biometrics data for each field are passed as base64 encoded string,
    and then saved as a Binary data in the database.
    """
    queryset = Biometrics.objects.all()
    serializer_class = BiometricSerializer

