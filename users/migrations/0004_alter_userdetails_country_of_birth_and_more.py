# Generated by Django 4.1.6 on 2023-02-05 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_userdetails_email_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='country_of_birth',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='current_occupation',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='employment_status',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='gender',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='is_minor',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='marital_status',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='postal_address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='primary_phone',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='residential_address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='town_of_birth',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
