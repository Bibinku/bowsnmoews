# Generated by Django 5.0.6 on 2024-08-15 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Petend', '0014_breaddb_bkci'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReplayDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('replay1', models.CharField(blank=True, max_length=100, null=True)),
                ('replay2', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]