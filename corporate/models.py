from django.contrib.auth.models import User
from django.db import models


class CorporateAgencyDetails(models.Model):
    """
    CorporateAgency model. Corporate Agency refers to a company or organization that is registered with the Digital Identity System.
    and wants to access user and business information, such as user  and identity verification.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_government = models.BooleanField(default=False)  # Whether the corporate agency is a government agency.
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    website = models.URLField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class CorporateAgencyDocuments(models.Model):
    """
    CorporateAgencyDocuments model. This model is used to store the documents uploaded by the corporate agency.
    """
    corporate_agency = models.ForeignKey(CorporateAgencyDetails, on_delete=models.CASCADE)
    document_name = models.CharField(max_length=100)
    document_file = models.FileField(upload_to='corporate_agency_documents/')

    def __str__(self):
        return self.corporate_agency.name


class OtherCorporateAgencyDetails(models.Model):
    """
    OtherCorporateAgencyDetails model. This model is used to store other details of the corporate agency.
    """
    corporate_agency = models.ForeignKey(CorporateAgencyDetails, on_delete=models.CASCADE)
    detail_key = models.CharField(max_length=100)
    details_value = models.CharField(max_length=100)

    def __str__(self):
        return self.corporate_agency.name


class CorporateAgencyTransaction(models.Model):
    """
    CorporateAgencyTransaction model. This model is used to store the transactions made by the corporate agency.
    """
    corporate_agency = models.ForeignKey(CorporateAgencyDetails, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=100)
    transaction_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return self.corporate_agency.name


class CorporateAgencyWallet(models.Model):
    """
    CorporateAgencyWallet model. This model is used to store the wallet of the corporate agency.
    """
    corporate_agency = models.OneToOneField(CorporateAgencyDetails, on_delete=models.CASCADE)
    available_balance = models.DecimalField(max_digits=12, decimal_places=2)
    maximum_balance = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.corporate_agency.name


class CorporateAgencyBiometrics(models.Model):
    """
    CorporateAgencyBiometrics model. This model is used to store the biometrics of the corporate agency.
    """
    corporate_agency = models.ForeignKey(CorporateAgencyDetails, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fingerprint = models.BinaryField(blank=True, null=True, unique=True)
    face = models.BinaryField(blank=True, null=True, unique=True)
    iris = models.BinaryField(blank=True, null=True, unique=True)
    voice = models.BinaryField(blank=True, null=True, unique=True)


def __str__(self):
    return self.corporate_agency.name
