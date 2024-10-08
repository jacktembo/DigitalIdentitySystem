import base64

from rest_framework import serializers
from rest_framework.authtoken.models import Token

from .models import *


class UserDetailsSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField(method_name='get_username')
    first_name = serializers.SerializerMethodField(method_name='get_first_name')
    last_name = serializers.SerializerMethodField(method_name='get_last_name')
    email_address = serializers.SerializerMethodField(method_name='get_email_address')

    @staticmethod
    def get_username(user_detail: UserDetails):
        return user_detail.user.username

    @staticmethod
    def get_first_name(user_detail: UserDetails):
        return user_detail.user.first_name

    @staticmethod
    def get_last_name(user_detail: UserDetails):
        return user_detail.user.last_name

    @staticmethod
    def get_email_address(user_detail: UserDetails):
        return user_detail.user.email

    class Meta:
        model = UserDetails
        fields = [
            'username', 'first_name', 'last_name', 'email_address',
            'user', 'date_of_birth', 'country_of_birth',
            'town_of_birth', 'gender', 'marital_status', 'national_id_number',
            'passport_number', 'driver_license_number', 'current_occupation', 'is_minor',
            'primary_phone', 'secondary_phone', 'website', 'facebook_profile_link',
            'instagram_profile_link', 'linkedIn_profile_link', 'twitter_handle',
            'youtube_channel_link', 'residential_address', 'postal_address', 'contact_person_name',
            'contact_person_phone', 'contact_person_address', 'employment_status', 'height',
            'year_completed_g7', 'year_completed_g9', 'year_completed_g12',
            'year_completed_diploma', 'year_completed_degree', 'year_completed_masters',
            'year_completed_phd', 'marks_obtained_g7', 'marks_obtained_g9', 'points_obtained_g12',

        ]


class UserDocumentSerializer(serializers.ModelSerializer):
    portrait_photo = serializers.FileField(use_url=True, required=False)
    national_id = serializers.FileField(use_url=True, required=False)
    passport = serializers.FileField(use_url=True, required=False)
    driving_license = serializers.FileField(use_url=True, required=False)
    tax_payer_registration = serializers.FileField(use_url=True, required=False)
    g7_results = serializers.FileField(use_url=True, required=False)
    g9_results = serializers.FileField(use_url=True, required=False)
    g12_results = serializers.FileField(use_url=True, required=False)
    school_diploma = serializers.FileField(use_url=True, required=False)
    school_degree = serializers.FileField(use_url=True, required=False)
    school_masters = serializers.FileField(use_url=True, required=False)
    school_phd = serializers.FileField(use_url=True, required=False)
    proof_of_residence = serializers.FileField(use_url=True, required=False)
    resume = serializers.FileField(use_url=True, required=False)
    medical_certificate = serializers.FileField(use_url=True, required=False)
    signature = serializers.FileField(use_url=True, required=False)

    class Meta:
        model = UserDocuments
        fields = [
            'user', 'portrait_photo', 'national_id', 'passport', 'driving_license',
            'tax_payer_registration', 'g7_results', 'g9_results', 'g12_results',
            'school_diploma', 'school_degree', 'school_masters', 'school_phd',
            'proof_of_residence', 'resume', 'medical_certificate', 'signature',
        ]


class BiometricSerializer(serializers.ModelSerializer):
    fingerprint = serializers.CharField(required=False)
    face = serializers.CharField(required=False)
    iris = serializers.CharField(required=False)
    voice = serializers.CharField(required=False)

    class Meta:
        model = Biometrics
        fields = [
            'user', 'fingerprint', 'face', 'iris', 'voice',
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
        fingerprint = validated_data.get('fingerprint', None)
        if fingerprint is not None:
            fingerprint = base64.b64decode(fingerprint)
        face = validated_data.get('face', None)
        if face is not None:
            face = base64.b64decode(face)
        iris = validated_data.get('iris', None)
        if iris is not None:
            iris = base64.b64decode(iris)
        voice = validated_data.get('voice', None)
        if voice is not None:
            voice = base64.b64decode(voice)

        user = validated_data.get('user', None)

        # Create an instance of the model
        instance = Biometrics()
        # Set the properties of the model
        instance.fingerprint = fingerprint
        instance.face = face
        instance.iris = iris
        instance.voice = voice
        instance.user = user
        # Save the instance to the database
        instance.save()
        return instance

    def to_representation(self, instance):
        """
        The binary data is encoded to base64 before being sent to the client.
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


class UserTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTransaction
        fields = [
            'user', 'date_time_created', 'transaction_type', 'description'
        ]


class UserTokenSerializer(serializers.ModelSerializer):
    token = serializers.CharField(source='key')

    class Meta:
        model = Token
        fields = ['token', ]


class UserWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserWallet
        fields = [
            'user', 'available_balance', 'maximum_balance'
        ]


class OtherUserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherUserDetails
        fields = [
            'user', 'detail_key', 'detail_value'
        ]


class OtherUserDocumentsSerializer(serializers.ModelSerializer):
    document_file = serializers.FileField(use_url=True)

    class Meta:
        model = OtherUserDocument
        fields = [
            'user', 'document_name', 'description', 'document_file',
        ]


class DigitalIdentityCardSerializer(serializers.ModelSerializer):
    first_name = serializers.SerializerMethodField(method_name='get_first_name')
    last_name = serializers.SerializerMethodField(method_name='get_last_name')
    date_of_birth = serializers.SerializerMethodField(method_name='get_dob')

    def get_first_name(self, identity_card: DigitalIdentityCard):
        return identity_card.user.first_name

    def get_last_name(self, identity_card: DigitalIdentityCard):
        return identity_card.user.last_name

    def get_dob(self, identity_card: DigitalIdentityCard):
        return identity_card.user.userdetails.date_of_birth

    class Meta:
        model = DigitalIdentityCard
        fields = [
            'user', 'first_name', 'last_name', 'date_of_birth',
            'registration_number', 'card_number', 'registration_date'
        ]
