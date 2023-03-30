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
        Overide the create method to convert the base64 data to binary.
        :param validated_data:
        :return:
        """
        fingerprint = validated_data.get('fingerprint', None)
        if fingerprint:
            fingerprint = base64.b64decode(fingerprint)
        face = validated_data.get('face', None)
        if face:
            face = base64.b64decode(face)
        iris = validated_data.get('iris', None)
        if iris:
            iris = base64.b64decode(iris)
        voice = validated_data.get('voice', None)
        if voice:
            voice = base64.b64decode(voice)
        business = validated_data.get('business', None)
        user = validated_data.get('user', None)

        instance = BusinessBiometrics()
        instance.fingerprint = fingerprint
        instance.face = face
        instance.iris = iris
        instance.voice = voice
        instance.business = business
        instance.user = user

        instance.save()
        return instance

    def to_representation(self, instance):
        """
        The binary data is converted to base64 before being sent to the client.
        :param instance:
        :return:
        """
        representation = super().to_representation(instance)
        if instance.fingerprint:
            representation['fingerprint'] = base64.b64encode(instance.fingerprint).decode('utf-8')
        if instance.face:
            representation['face'] = base64.b64encode(instance.face).decode('utf-8')
        if instance.iris:
            representation['iris'] = base64.b64encode(instance.iris).decode('utf-8')
        if instance.voice:
            representation['voice'] = base64.b64encode(instance.voice).decode('utf-8')
        return representation
