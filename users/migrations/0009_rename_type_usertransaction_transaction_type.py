# Generated by Django 4.1.7 on 2023-03-11 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0008_digitalidentitycard"),
    ]

    operations = [
        migrations.RenameField(
            model_name="usertransaction",
            old_name="type",
            new_name="transaction_type",
        ),
    ]