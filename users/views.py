from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404, get_list_or_404
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

