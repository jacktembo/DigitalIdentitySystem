from django.contrib.auth.models import User
from django.db import models


class Business(models.Model):
    """
    A Company or business that wants to use the digital identity system.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    postal_address = models.CharField(max_length=255)
    registered_office_address = models.CharField(max_length=255)
    date_registered = models.DateField()
    registration_number = models.CharField(max_length=50)
    tax_payer_number = models.CharField(max_length=20)
    business_type = models.CharField(max_length=50)
    nature_of_business = models.TextField()
    contact_number = models.CharField(max_length=15)
    email_address = models.EmailField(max_length=64)
    contact_person_name = models.CharField(max_length=255)
    contact_person_phone = models.CharField(max_length=255)
    contact_person_address = models.CharField(max_length=255)
    contact_person_role = models.CharField(max_length=255)
    contact_person_email = models.EmailField(max_length=64)
    website = models.URLField(max_length=255, blank=True, null=True)
    facebook_url = models.URLField(max_length=255, null=True, blank=True)
    linkedIn_url = models.URLField(max_length=255, blank=True, null=True)
    youtube_url = models.URLField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class BusinessDocuments(models.Model):
    business = models.OneToOneField(Business, on_delete=models.CASCADE)
    incorporation_certificate = models.FileField(upload_to='business/IncorporationCertificates')
    tax_payer_identification = models.FileField(upload_to='institution/tpin')
    profile = models.FileField(upload_to='institution/profile', null=True, blank=True)
    articles_of_association = models.FileField(upload_to='institution/Articles', null=True, blank=True)
    bank_statement = models.FileField(upload_to='business/BankStatement', null=True, blank=True)
    logo = models.ImageField(upload_to='business/logos', blank=True, null=True)


    def __str__(self):
        return self.business


class OtherBusinessDetails(models.Model):
    """
    Other business details that have not been included in the Business model.
    These are custom business details that are specific for certain institutions or businesses.
    """
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    key = models.CharField(max_length=255)
    value = models.CharField(max_length=255)


class OtherBusinessDocuments(models.Model):
    """
    Other business documents that have not been included in the BusinessDocuments model.
    These include documents that are specific to a certain business or firm.
    """
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    document_name = models.CharField(max_length=255)
    document_file = models.FileField(upload_to='business/OtherDocuments')


class BusinessWallet(models.Model):
    business = models.OneToOneField(Business, on_delete=models.CASCADE)
    available_balance = models.DecimalField(max_digits=12, decimal_places=2)
    maximum_balance = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.business} Account"

