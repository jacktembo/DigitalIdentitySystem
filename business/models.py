from django.contrib.auth.models import User
from django.db import models


class Business(models.Model):
    """
    A Company or Agency that opts to identify its clients with digital identity system.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    postal_address = models.CharField(max_length=255)
    registration_number = models.CharField(max_length=50)
    tax_payer_number = models.CharField(max_length=20)
    business_type = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=15)
    email_address = models.EmailField(max_length=64)

    def __str__(self):
        return self.name


class BusinessDocuments(models.Model):
    business = models.OneToOneField(Business, on_delete=models.CASCADE)
    incorporation_certificate = models.FileField(upload_to='business/IncorporationCertificates')
    tax_payer_identification = models.FileField(upload_to='institution/tpin')
    profile = models.FileField(upload_to='institution/profile')
    articles_of_association = models.FileField(upload_to='institution/Articles')

    def __str__(self):
        return self.business


