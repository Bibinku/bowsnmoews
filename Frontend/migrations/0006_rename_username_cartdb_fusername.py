# Generated by Django 5.0.6 on 2024-08-01 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0005_cartdb'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartdb',
            old_name='username',
            new_name='fusername',
        ),
    ]