from django.db.models import QuerySet
from rest_framework import permissions, viewsets

from .serializers import *


class ReadOnlyNonSuperuserPermission(permissions.BasePermission):
    """
    Custom permission to allow only superusers to create, delete and update objects.
    Other authenticated users can only perform safe operations such as GET, HEAD, OPTIONS.
    """

    def has_permission(self, request, view):
        unsafe_request_methods = ['DELETE', 'PUT', 'POST', 'PATCH']
        safe_request_methods = ['GET', 'HEAD']
        # Allow POST, PUT, PATCH and DELETE methods only to superusers.
        if request.method in unsafe_request_methods and request.user.is_superuser:
            return True
        elif request.method in safe_request_methods:
            return True
        return False


def get_user_queryset(request, model) -> QuerySet:
    """
    Get a queryset depending on whether the requesting user is superuser. If is superuser,
    return all the matching objects. Otherwise, only return objects owned by the requesting user.
    :param request:
    :param model:
    :return:
    """
    user = request.user
    if user.is_superuser:
        return model.objects.all()
    return model.objects.filter(user=user)


def get_business_queryset(request, model) -> QuerySet:
    """
    Get a queryset depending on whether the requesting user is superuser. If is superuser,
    return all the matching objects. Otherwise, only return objects owned by the requesting user.
    :param request:
    :param model:
    :return:
    """
    user = request.user
    if user.is_superuser:
        return model.objects.all()
    return model.objects.filter(business__user=user)


class BusinessViewSet(viewsets.ModelViewSet):
    """
    A viewset for listing, creating, updating and deleting businesses.
    """

    def get_queryset(self):
        return get_user_queryset(self.request, Business)

    serializer_class = BusinessSerializer
    permission_classes = [ReadOnlyNonSuperuserPermission, permissions.IsAuthenticated]


class BusinessDocumentsViewSet(viewsets.ModelViewSet):
    """
    A viewset for listing, creating, updating and deleting business documents.
    """

    def get_queryset(self):
        return get_business_queryset(self.request, BusinessDocuments)

    serializer_class = BusinessDocumentsSerializer
    permission_classes = [ReadOnlyNonSuperuserPermission, permissions.IsAuthenticated]


class OtherBusinessDetailsViewSet(viewsets.ModelViewSet):
    """
    A viewset for listing, creating, updating and deleting other business details.
    """

    def get_queryset(self):
        return get_business_queryset(self.request, OtherBusinessDetails)

    serializer_class = OtherBusinessDetailsSerializer
    permission_classes = [ReadOnlyNonSuperuserPermission, permissions.IsAuthenticated]


class OtherBusinessDocumentsViewSet(viewsets.ModelViewSet):
    """
    A viewset for listing, creating, updating and deleting other business documents.
    """

    def get_queryset(self):
        return get_business_queryset(self.request, OtherBusinessDocuments)

    serializer_class = OtherBusinessDocumentsSerializer
    permission_classes = [ReadOnlyNonSuperuserPermission, permissions.IsAuthenticated]


class BusinessWalletViewSet(viewsets.ModelViewSet):
    """
    A viewset for listing, creating, updating and deleting other business details.
    """

    def get_queryset(self):
        return get_business_queryset(self.request, BusinessWallet)

    serializer_class = BusinessWalletSerializer
    permission_classes = [ReadOnlyNonSuperuserPermission, permissions.IsAuthenticated]


class TransactionViewSet(viewsets.ModelViewSet):
    """
    A viewset for listing, creating, updating and deleting other business transactions.
    """

    def get_queryset(self):
        return get_business_queryset(self.request, Transaction)

    serializer_class = TransactionSerializer
    permission_classes = [ReadOnlyNonSuperuserPermission, permissions.IsAuthenticated]
