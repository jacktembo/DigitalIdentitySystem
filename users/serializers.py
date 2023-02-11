from rest_framework import serializers
from .models import *
import base64


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

    class Meta:
        model = UserDocuments
        fields = [
            'user', 'portrait_photo', 'national_id', 'passport', 'driving_license',
            'tax_payer_registration', 'g7_results', 'g9_results', 'g12_results',
            'school_diploma', 'school_degree', 'school_masters', 'school_phd',
            'proof_of_residence', 'resume', 'medical_certificate',
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
        fingerprint = base64.b64decode(validated_data['fingerprint'])
        face = base64.b64decode(validated_data.get('face', None))
        iris = base64.b64decode(validated_data.get('iris', None))
        voice = base64.b64decode(validated_data.get('voice', None))
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
