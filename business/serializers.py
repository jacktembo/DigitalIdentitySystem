import base64

from rest_framework import serializers

from .models import *


class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = [
            'id', 'name', 'user', 'postal_address', 'registered_office_address', 'date_registered',
            'registration_number', 'tax_payer_number', 'business_type', 'nature_of_business',
            'contact_number', 'email_address', 'contact_person_name', 'contact_person_phone',
            'contact_person_address', 'contact_person_role', 'contact_person_email', 'website',
            'facebook_url', 'linkedIn_url', 'youtube_url',
        ]


class BusinessDocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessDocuments
        fields = [
            'id', 'business', 'incorporation_certificate', 'tax_payer_identification',
            'profile', 'articles_of_association', 'bank_statement', 'logo',
        ]


class OtherBusinessDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherBusinessDetails
        fields = [
            'id', 'business', 'key', 'value',
        ]


class OtherBusinessDocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherBusinessDocuments
        fields = [
            'id', 'business', 'document_name', 'document_file',
        ]


class BusinessWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessWallet
        fields = [
            'id', 'business', 'available_balance', 'maximum_balance',
        ]


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = [
            'business', 'id', 'date_time_created', 'transaction_type', 'description',
        ]


class BusinessBiometricsSerializer(serializers.ModelSerializer):
    fingerprint = serializers.CharField(required=False)
    face = serializers.CharField(required=False)
    iris = serializers.CharField(required=False)
    voice = serializers.CharField(required=False)

    class Meta:
        model = BusinessBiometrics
        fields = [
            'business', 'user', 'fingerprint', 'face', 'voice', 'iris',
        ]

    def create(self, validated_data):
        """
        The string data passed to the api should be base64 encoded, and then
        it's decoded as binary data before being saved. Clients should always
        encode the string to base64 before sending it to the API.
        :param validated_data:
        :return:
        """
        # Decode the base64 encoded data
        global fingerprint, face, iris, voice
        if 'fingerprint' in validated_data:
            fingerprint = base64.b64decode(validated_data['fingerprint'])
        if 'face' in validated_data:
            face = base64.b64decode(validated_data['face'])
        if 'iris' in validated_data:
            iris = base64.b64decode(validated_data['iris'])
        if 'voice' in validated_data:
            voice = base64.b64decode(validated_data['voice'])

        user = validated_data.get('user', None)
        business = validated_data.get('business', None)
        # Create an instance of the model
        instance = BusinessBiometrics()
        # Set the properties of the model
        if 'fingerprint' in validated_data:
            instance.fingerprint = fingerprint
        if 'face' in validated_data:
            instance.face = face
        if 'iris' in validated_data:
            instance.iris = iris
        if 'voice' in validated_data:
            instance.voice = voice
        if user is not None:
            instance.user = user
        if business is not None:
            instance.business = business
        # Save the instance to the database
        instance.save()
        return instance


