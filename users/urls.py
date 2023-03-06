from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()
router.register(r'details', UserDetailsViewSet, basename='details')
router.register(r'documents', UserDocumentViewSet, basename='documents')
router.register(r'biometrics', BiometricsViewSet, basename='biometrics')
router.register(r'transactions', UserTransactionViewSet, basename='transactions')
router.register(r'wallets',UserWalletViewSet, basename='wallets')
router.register(r'other-details', OtherUserDetailsViewSet, basename='other-details')
router.register(r'other-documents', OtherUserDocumentViewSet, basename='other-documentss')


urlpatterns = [
    path('', include(router.urls)),
    path('biometric-login', views.BiometricLogin.as_view()),
]
