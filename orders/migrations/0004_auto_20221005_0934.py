# Generated by Django 3.1 on 2022-10-05 04:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20220927_1934'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderproduct',
            old_name='variation',
            new_name='variations',
        ),
    ]
