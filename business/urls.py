from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'details', views.BusinessViewSet, basename='business-details')
router.register(r'documents', views.BusinessDocumentsViewSet, basename='business-documents')
router.register(r'other-details', views.OtherBusinessDetailsViewSet, basename='other-details')
router.register(r'other-documents', views.OtherBusinessDocumentsViewSet, basename='other-documents')
router.register(r'wallets', views.BusinessWalletViewSet, basename='wallets')
router.register(r'transactions', views.TransactionViewSet, basename='transactions')
router.register(r'biometrics', views.BusinessBiometricsViewSet, basename='biometrics')

urlpatterns = [
    path('', include(router.urls)),
]
