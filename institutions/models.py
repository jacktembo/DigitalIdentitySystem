from django.contrib.auth.models import User
from django.db import models


class Institution(models.Model):
    """
    A Company or Agency that opts to identify its clients with digital identity system.
    """
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    postal_address = models.CharField(max_length=255)
    registration_number = models.CharField(max_length=50)
    tax_payer_number = models.CharField(max_length=20)
    institution_type = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=15)
    email_address = models.EmailField(max_length=64)

    def __str__(self):
        return self.name


class InstitutionDocuments(models.Model):
    institution = models.OneToOneField(Institution, on_delete=models.CASCADE)
    incorporation_certificate = models.FileField(upload_to='institutions/IncorporationCertificates')
    tax_payer_identification = models.FileField(upload_to='institution/tpin')
    profile = models.FileField(upload_to='institution/profile')
    articles_of_association = models.FileField(upload_to='institution/Articles')

    def __str__(self):
        return self.institution


