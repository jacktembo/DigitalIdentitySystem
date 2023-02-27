from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
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


class UserTransactionViewSet(viewsets.ModelViewSet):
    """
    Transactions made by or to the user's account.
    """
    queryset = UserTransaction.objects.all()
    serializer_class = UserTransactionSerializer


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


class WebsiteLoginView(APIView):
    """
    This endpoint allows users to signup and sign in to various websites
    and apps using digital identity. The user is redirected to the digital
    identity login page, and logs in using their username and password combination,
    or their biometrics such as fingerprint. After successful login, we shall return
    the required personal details about the user.
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
    queryset = UserWallet.objects.all()

    def get_serializer_class(self):
        return UserWalletSerializer

    lookup_field = 'user'


