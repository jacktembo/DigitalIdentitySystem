from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import UserDetailsViewSet, UserDocumentViewSet, BiometricsViewSet


router = DefaultRouter()
router.register(r'details', UserDetailsViewSet)
router.register(r'documents', UserDocumentViewSet)
router.register(r'biometrics', BiometricsViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
