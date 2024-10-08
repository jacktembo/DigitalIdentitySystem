import random
from _decimal import Decimal

from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.db.models import QuerySet
from django.shortcuts import get_object_or_404, render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

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


class UserDetailsViewSet(viewsets.ModelViewSet):
    """
    This Viewset is responsible for creating, reading, updating, and deleting
    UserDetails objects.
    You can get a specific user using the 'national_id_number' lookup field.
    """

    def get_queryset(self):
        return get_user_queryset(self.request, UserDetails)

    serializer_class = UserDetailsSerializer
    permission_classes = [ReadOnlyNonSuperuserPermission, permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]


class UserDocumentViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return get_user_queryset(self.request, UserDocuments)

    serializer_class = UserDocumentSerializer
    permission_classes = [ReadOnlyNonSuperuserPermission, permissions.IsAuthenticated]


class BiometricsViewSet(viewsets.ModelViewSet):
    """
    The biometrics data for each field are passed as base64 encoded string,
    and then saved as a Binary data in the database.
    """

    def get_queryset(self):
        return get_user_queryset(self.request, Biometrics)

    serializer_class = BiometricSerializer
    permission_classes = [ReadOnlyNonSuperuserPermission, permissions.IsAuthenticated]


class UserTransactionViewSet(viewsets.ModelViewSet):
    """
    Transactions made by or to the user's account.
    """

    def get_queryset(self):
        return get_user_queryset(self.request, UserTransaction)

    serializer_class = UserTransactionSerializer
    permission_classes = [ReadOnlyNonSuperuserPermission, permissions.IsAuthenticated]


class BiometricLogin(APIView):
    """
            Pass the channel and data in the request body. Channel is the biometric channel
            to be used. For example: fingerprint, face, voice, iris, etc.
            data is the base64 encoded string of the biometric data such as fingerprint.
            :param channel, data:
            :return: token
            """

    def post(self, request):

        channel = request.data.get('channel', None)
        data = request.data.get('data', None)

        if channel == "fingerprint":
            fingerprint = base64.b64decode(data)
            user = get_object_or_404(User, biometrics__fingerprint=fingerprint)
            token = get_object_or_404(Token, user=user).key
            return Response({'token': token})

        elif channel == "face":
            face = base64.b64decode(data)
            user = get_object_or_404(User, biometrics__face=face)
            token = get_object_or_404(Token, user=user).key
            return Response({'token': token})

        elif channel == "iris":
            iris = base64.b64decode(data)
            user = get_object_or_404(User, biometrics__iris=iris)
            token = get_object_or_404(Token, user=user).key
            return Response({'token': token})

        elif channel == "voice":
            voice = base64.b64decode(data)
            user = get_object_or_404(User, biometrics__voice=voice)
            token = get_object_or_404(Token, user=user).key
            return Response({'token': token})


class OAuth(APIView):
    """
    This endpoint allows users to signup and sign in to various websites
    and apps using digital identity. The user is redirected to the digital
    identity login page, and logs in using their username and password combination,
    or their biometrics such as fingerprint. After successful login,
    the user will grant access of their data to the third party application,
     and we shall make a POST request to the provided call back URL passing the
     user data and the certain token in the Post request. The third party application must save
     the token we POST, and each time a user logs in with digital identity, we shall be returning
     this token. The callback URL must return a redirect URl in the response, where we shall finally
    redirect the user.
    """

    def post(self, request, format=None):
        channel = request.data.get("channel", None)
        data = request.data.get('data', None)
        if channel == "basic":
            # Extract the username and password from the request body
            username = request.data.get('username')
            password = request.data.get('password')

            # Authenticate the user using the provided credentials
            user = authenticate(username=username, password=password)

            # If authentication was successful, return the user's first name
            if user is not None:
                return Response(
                    {
                        'first_name': user.first_name, 'last_name': user.last_name,
                        'national_id_number': user.userdetails.national_id_number,
                        'email': user.email, 'date_of_birth': user.userdetails.date_of_birth,
                        'residential_address': user.userdetails.residential_address,
                        'postal_address': user.userdetails.postal_address,
                        'nationality': user.userdetails.country_of_birth,
                        'phone_number': user.userdetails.primary_phone, 'gender': user.userdetails.gender,
                        'marital_status': user.userdetails.marital_status,
                    }
                )
            # Otherwise, return an error message
            else:
                return Response({'error': 'Invalid credentials'}, status=401)

        elif channel == "fingerprint":
            fingerprint = base64.b64decode(data)
            user = get_object_or_404(User, biometrics__fingerprint=fingerprint)
            return Response(
                {
                    'first_name': user.first_name, 'last_name': user.last_name,
                    'national_id_number': user.userdetails.national_id_number,
                    'email': user.email, 'date_of_birth': user.userdetails.date_of_birth,
                    'residential_address': user.userdetails.residential_address,
                    'postal_address': user.userdetails.postal_address,
                    'nationality': user.userdetails.country_of_birth,
                    'phone_number': user.userdetails.primary_phone, 'gender': user.userdetails.gender,
                    'marital_status': user.userdetails.marital_status,
                }
            )

        elif channel == "face":
            face = base64.b64decode(data)
            user = get_object_or_404(User, biometrics__face=face)
            return Response(
                {
                    'first_name': user.first_name, 'last_name': user.last_name,
                    'national_id_number': user.userdetails.national_id_number,
                    'email': user.email, 'date_of_birth': user.userdetails.date_of_birth,
                    'residential_address': user.userdetails.residential_address,
                    'postal_address': user.userdetails.postal_address,
                    'nationality': user.userdetails.country_of_birth,
                    'phone_number': user.userdetails.primary_phone, 'gender': user.userdetails.gender,
                    'marital_status': user.userdetails.marital_status,
                }
            )

        elif channel == "iris":
            iris = base64.b64decode(data)
            user = get_object_or_404(User, biometrics__iris=iris)
            return Response(
                {
                    'first_name': user.first_name, 'last_name': user.last_name,
                    'national_id_number': user.userdetails.national_id_number,
                    'email': user.email, 'date_of_birth': user.userdetails.date_of_birth,
                    'residential_address': user.userdetails.residential_address,
                    'postal_address': user.userdetails.postal_address,
                    'nationality': user.userdetails.country_of_birth,
                    'phone_number': user.userdetails.primary_phone, 'gender': user.userdetails.gender,
                    'marital_status': user.userdetails.marital_status,
                }
            )

        elif channel == "voice":
            voice = base64.b64decode(data)
            user = get_object_or_404(User, biometrics__voice=voice)
            return Response(
                {
                    'first_name': user.first_name, 'last_name': user.last_name,
                    'national_id_number': user.userdetails.national_id_number,
                    'email': user.email, 'date_of_birth': user.userdetails.date_of_birth,
                    'residential_address': user.userdetails.residential_address,
                    'postal_address': user.userdetails.postal_address,
                    'nationality': user.userdetails.country_of_birth,
                    'phone_number': user.userdetails.primary_phone, 'gender': user.userdetails.gender,
                    'marital_status': user.userdetails.marital_status,
                }
            )


class UserWalletViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return get_user_queryset(self.request, UserWallet)

    def get_serializer_class(self):
        return UserWalletSerializer

    lookup_field = 'user'
    permission_classes = [ReadOnlyNonSuperuserPermission, permissions.IsAuthenticated]


class OtherUserDetailsViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return get_user_queryset(self.request, OtherUserDetails)

    def get_serializer_class(self):
        return OtherUserDetailsSerializer

    permission_classes = [ReadOnlyNonSuperuserPermission, permissions.IsAuthenticated]


class OtherUserDocumentViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return get_user_queryset(self.request, OtherUserDocument)

    def get_serializer_class(self):
        return OtherUserDocumentsSerializer

    permission_classes = [ReadOnlyNonSuperuserPermission, permissions.IsAuthenticated]


def oauth_login(request):
    if request.method == 'GET':
        context = {}
        return render(request, 'OAuth_login.html', context)


class DigitalIdentityCardViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return get_user_queryset(self.request, DigitalIdentityCard)

    def get_serializer_class(self):
        return DigitalIdentityCardSerializer

    permission_classes = [ReadOnlyNonSuperuserPermission, permissions.IsAuthenticated]


class WalletTopUp(APIView):
    """
    Deposit funds into user wallet.
    """
    permission_classes = [ReadOnlyNonSuperuserPermission]

    def post(self, request, format=None):
        """
        :data recipient_username, amount
        :param request:
        :param format:
        :return:
        """
        # Get the user's wallet from the request user
        user_wallet = UserWallet.objects.get(user__username=request.data.get('recipient_username'))

        # Get the amount to top up from the request data
        amount = request.data.get('amount', None)

        # Ensure amount is provided and valid
        if amount is None:
            return Response({'error': 'Amount is required'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            amount = Decimal(amount)
        except ValueError:
            return Response({'error': 'Invalid amount'}, status=status.HTTP_400_BAD_REQUEST)

        # Ensure top up amount is within the maximum balance limit
        if user_wallet.available_balance + amount > user_wallet.maximum_balance:
            return Response({'error': 'Maximum balance exceeded'}, status=status.HTTP_400_BAD_REQUEST)

        # Update the user's balance
        user_wallet.available_balance += amount
        user_wallet.save()

        # Return a success response
        return Response({'success': 'Top-up successful'}, status=status.HTTP_200_OK)


class SendMoney(APIView):
    """
    Send money from one user account to another.
    """
    def post(self, request, format=None):
        # Get the sender and recipient's wallets from the request data
        sender_wallet = UserWallet.objects.get(user=request.user)
        recipient_username = request.data.get('recipient', None)
        if recipient_username is None:
            return Response({'error': 'Recipient is required'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            recipient_user = User.objects.get(username=recipient_username)
            recipient_wallet = UserWallet.objects.get(user=recipient_user)
        except (User.DoesNotExist, UserWallet.DoesNotExist):
            return Response({'error': 'Invalid recipient'}, status=status.HTTP_400_BAD_REQUEST)

        # Get the amount to send from the request data
        amount = request.data.get('amount', None)

        # Ensure amount is provided and valid
        if amount is None:
            return Response({'error': 'Amount is required'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            amount = Decimal(amount)
        except ValueError:
            return Response({'error': 'Invalid amount'}, status=status.HTTP_400_BAD_REQUEST)

        # Ensure sender has sufficient funds
        if amount > sender_wallet.available_balance:
            return Response({'error': 'Insufficient funds'}, status=status.HTTP_400_BAD_REQUEST)

        # Ensure recipient maximum balance is not exceeded
        if recipient_wallet.available_balance + amount > recipient_wallet.maximum_balance:
            return Response({'error': 'Recipient maximum balance exceeded'}, status=status.HTTP_400_BAD_REQUEST)

        # Transfer funds from sender to recipient
        sender_wallet.available_balance -= amount
        recipient_wallet.available_balance += amount
        sender_wallet.save()
        recipient_wallet.save()

        # Return a success response
        return Response({'success': 'Money sent successfully'}, status=status.HTTP_200_OK)

