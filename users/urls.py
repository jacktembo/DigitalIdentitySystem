from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()
router.register(r'details', UserDetailsViewSet, basename='user-details')
router.register(r'documents', UserDocumentViewSet, basename='user-documents')
router.register(r'biometrics', BiometricsViewSet, basename='user-biometrics')
router.register(r'transactions', UserTransactionViewSet, basename='user-transactions')
router.register(r'wallets', UserWalletViewSet, basename='user-wallets')
router.register(r'other-details', OtherUserDetailsViewSet, basename='other-user-details')
router.register(r'other-documents', OtherUserDocumentViewSet, basename='other-user-documents')
router.register(r'identity-cards', DigitalIdentityCardViewSet, basename='user-digital-identity-cards')


urlpatterns = [
    path('', include(router.urls)),
    path('biometric-login', views.BiometricLogin.as_view()),
    path('OAuth', views.oauth_login, name='oauth-login'),
    path('wallet-topup/', views.WalletTopUp.as_view()),
    path('send-money', views.SendMoney.as_view()),
]
