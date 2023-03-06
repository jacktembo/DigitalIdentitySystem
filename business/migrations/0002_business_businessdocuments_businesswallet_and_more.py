# Generated by Django 4.1.7 on 2023-03-05 14:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("business", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Business",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("postal_address", models.CharField(max_length=255)),
                ("registered_office_address", models.CharField(max_length=255)),
                ("date_registered", models.DateField()),
                ("registration_number", models.CharField(max_length=50)),
                ("tax_payer_number", models.CharField(max_length=20)),
                ("business_type", models.CharField(max_length=50)),
                ("nature_of_business", models.TextField()),
                ("contact_number", models.CharField(max_length=15)),
                ("email_address", models.EmailField(max_length=64)),
                ("contact_person_name", models.CharField(max_length=255)),
                ("contact_person_phone", models.CharField(max_length=255)),
                ("contact_person_address", models.CharField(max_length=255)),
                ("contact_person_role", models.CharField(max_length=255)),
                ("contact_person_email", models.EmailField(max_length=64)),
                ("website", models.URLField(blank=True, max_length=255, null=True)),
                (
                    "facebook_url",
                    models.URLField(blank=True, max_length=255, null=True),
                ),
                (
                    "linkedIn_url",
                    models.URLField(blank=True, max_length=255, null=True),
                ),
                ("youtube_url", models.URLField(blank=True, max_length=255, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BusinessDocuments",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "incorporation_certificate",
                    models.FileField(upload_to="business/IncorporationCertificates"),
                ),
                (
                    "tax_payer_identification",
                    models.FileField(upload_to="institution/tpin"),
                ),
                (
                    "profile",
                    models.FileField(
                        blank=True, null=True, upload_to="institution/profile"
                    ),
                ),
                (
                    "articles_of_association",
                    models.FileField(
                        blank=True, null=True, upload_to="institution/Articles"
                    ),
                ),
                (
                    "bank_statement",
                    models.FileField(
                        blank=True, null=True, upload_to="business/BankStatement"
                    ),
                ),
                (
                    "logo",
                    models.ImageField(
                        blank=True, null=True, upload_to="business/logos"
                    ),
                ),
                (
                    "business",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="business.business",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BusinessWallet",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "available_balance",
                    models.DecimalField(decimal_places=2, max_digits=12),
                ),
                (
                    "maximum_balance",
                    models.DecimalField(decimal_places=2, max_digits=12),
                ),
                (
                    "business",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="business.business",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OtherBusinessDetails",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("key", models.CharField(max_length=255)),
                ("value", models.CharField(max_length=255)),
                (
                    "business",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="business.business",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OtherBusinessDocuments",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("document_name", models.CharField(max_length=255)),
                (
                    "document_file",
                    models.FileField(upload_to="business/OtherDocuments"),
                ),
                (
                    "business",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="business.business",
                    ),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name="institutiondocuments",
            name="institution",
        ),
        migrations.DeleteModel(
            name="Institution",
        ),
        migrations.DeleteModel(
            name="InstitutionDocuments",
        ),
    ]