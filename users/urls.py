from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()
router.register(r'details', UserDetailsViewSet)
router.register(r'documents', UserDocumentViewSet)
router.register(r'biometrics', BiometricsViewSet)
router.register(r'transactions', UserTransactionViewSet)
router.register(r'wallets',UserWalletViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('biometric-login', views.BiometricLogin.as_view()),
]
