# Generated by Django 5.1.3 on 2024-11-28 22:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_member_consent_for_data_use_and_storage_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='consent_for_data_use_and_storage',
            new_name='consent_data',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='consent_to_participate',
            new_name='consent_participate',
        ),
    ]
