from rest_framework import serializers
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
