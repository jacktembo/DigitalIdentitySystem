from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserDetails(models.Model):
    """ Personal details about the user who is registering with the system.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    country_of_birth = models.CharField(max_length=255, blank=True, null=True)
    town_of_birth = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=255, blank=True, null=True)
    marital_status = models.CharField(max_length=255, blank=True, null=True)
    national_id_number = models.CharField(max_length=255, blank=True, null=True)
    passport_number = models.CharField(max_length=255, blank=True, null=True)
    driver_license_number = models.CharField(max_length=255, blank=True, null=True)
    current_occupation = models.CharField(max_length=255, blank=True, null=True)
    is_minor = models.BooleanField(default=False, blank=True, null=True)
    primary_phone = models.CharField(max_length=255, blank=True, null=True)
    secondary_phone = models.CharField(max_length=255, blank=True, null=True)
    website = models.URLField(max_length=255, blank=True, null=True)
    facebook_profile_link = models.URLField(max_length=255, blank=True, null=True)
    instagram_profile_link = models.URLField(max_length=255, blank=True, null=True)
    linkedIn_profile_link = models.URLField(max_length=255, blank=True, null=True)
    twitter_handle = models.CharField(max_length=255, blank=True, null=True)
    youtube_channel_link = models.URLField(max_length=255, blank=True, null=True)
    residential_address = models.CharField(max_length=255, blank=True, null=True)
    postal_address = models.CharField(max_length=255, blank=True, null=True)
    contact_person_name = models.CharField(max_length=255, null=True, blank=True)
    contact_person_phone = models.CharField(max_length=255, null=True, blank=True)
    contact_person_address = models.CharField(max_length=255, blank=True, null=True)
    employment_status = models.CharField(max_length=255, blank=True, null=True)
    height = models.IntegerField(null=True, blank=True)
    # Educational details here
    year_completed_g7 = models.IntegerField(blank=True, null=True)  # Year a user completed their Grade Seven
    year_completed_g9 = models.IntegerField(blank=True, null=True)  # Year a user completed their Grade Nine
    year_completed_g12 = models.IntegerField(blank=True, null=True)  # Year a user completed their Grade Twelve
    year_completed_diploma = models.IntegerField(blank=True, null=True)
    year_completed_degree = models.IntegerField(blank=True, null=True)
    year_completed_masters = models.IntegerField(blank=True, null=True)
    year_completed_phd = models.IntegerField(blank=True, null=True)
    marks_obtained_g7 = models.IntegerField(blank=True, null=True)
    marks_obtained_g9 = models.IntegerField(blank=True, null=True)
    points_obtained_g12 = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        """
        Create the user details profile whenever the new user is created.
        :param instance:
        :param created:
        :param kwargs:
        :return:
        """
        if created:
            UserDetails.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.userdetails.save()

    class Meta:
        verbose_name_plural = 'UserDetails'


class UserDocuments(models.Model):
    """
    Relevant documents for a user.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    portrait_photo = models.FileField(upload_to='users/PortraitPhotos', blank=True, null=True)
    national_id = models.FileField(upload_to='users/NationalIds', blank=True, null=True)
    passport = models.FileField(upload_to='users/Passports', blank=True, null=True)
    driving_license = models.FileField(upload_to='users/DrivingLicense', blank=True, null=True)
    tax_payer_registration = models.FileField(upload_to='users/TPIN', blank=True, null=True)
    g7_results = models.FileField(upload_to='users/G7Results', blank=True, null=True)
    g9_results = models.FileField(upload_to='users/G9Results', blank=True, null=True)
    g12_results = models.FileField(upload_to='users/G12Results', blank=True, null=True)
    school_diploma = models.FileField(upload_to='users/SchoolDiplomas', blank=True, null=True)
    school_degree = models.FileField(upload_to='users/SchoolDegree', blank=True, null=True)
    school_masters = models.FileField(upload_to='users/users/SchoolMasters', blank=True, null=True)
    school_phd = models.FileField(upload_to='users/SchoolPHD', blank=True, null=True)
    proof_of_residence = models.FileField(upload_to='users/ResidenceProof', null=True, blank=True)
    resume = models.FileField(upload_to='users/Resumes', null=True, blank=True)
    medical_certificate = models.FileField(upload_to='users/MedicalCertificates', blank=True, null=True)
    signature = models.FileField(upload_to='users/Signatures', null=True, blank=True)

    def __str__(self):
        return f"personal details for {self.user}"

    class Meta:
        verbose_name_plural = 'User Documents'


class Biometrics(models.Model):
    """
    This is the models for all the biometrics of the user.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fingerprint = models.BinaryField(unique=True)
    face = models.BinaryField(blank=True, null=True, unique=True)
    iris = models.BinaryField(blank=True, null=True, unique=True)
    voice = models.BinaryField(blank=True, null=True, unique=True)

    class Meta:
        verbose_name_plural = 'Biometrics'


class UserTransaction(models.Model):
    """
    Transactions authorized by the user
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_time_created = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=255)
    description = models.CharField(max_length=255)


class UserWallet(models.Model):
    """
    User Account built in Wallet: users can deposit funds into their digital identity wallet
    and use the funds to pay for various products and services across the digital
    identity network. Funds can be deposited using mobile money, cash, bank transfer,
    etc.

    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    available_balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    maximum_balance = models.DecimalField(max_digits=12, decimal_places=2, default=100000)

    def __str__(self):
        return f"{self.user.username} Account"


class OtherUserDetails(models.Model):
    """
    Other user details that were not listed in UserDetails model. This includes
    any other information about the user that is not listed.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    detail_key = models.CharField(max_length=255) # The name or title of that key. For example: first_name
    detail_value = models.CharField(max_length=255) # The value for the key mentioned above. For example: Jack

    def __str__(self):
        return self.detail_key


class OtherUserDocument(models.Model):
    """
    Other user documents that were not included in the UserDocument model.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    document_name = models.CharField(max_length=255)
    document_file = models.FileField(upload_to='users/OtherDocuments')
    description = models.TextField()

    def __str__(self):
        return self.document_name

