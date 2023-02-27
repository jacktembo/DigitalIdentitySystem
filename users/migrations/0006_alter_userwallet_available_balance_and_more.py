# Generated by Django 4.1.7 on 2023-02-26 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_userdocuments_signature_userwallet_usertransaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userwallet',
            name='available_balance',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='userwallet',
            name='maximum_balance',
            field=models.DecimalField(decimal_places=2, default=100000, max_digits=12),
        ),
    ]