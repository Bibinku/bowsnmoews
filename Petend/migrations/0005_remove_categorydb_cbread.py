# Generated by Django 5.0.6 on 2024-07-04 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Petend', '0004_alter_breaddb_bage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categorydb',
            name='cbread',
        ),
    ]