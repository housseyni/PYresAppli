# Generated by Django 5.0.4 on 2024-04-11 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resApp', '0005_remove_evenement_created_by_email_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evenement',
            old_name='user',
            new_name='author',
        ),
    ]
