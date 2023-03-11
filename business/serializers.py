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