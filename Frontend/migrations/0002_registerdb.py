# Generated by Django 5.0.6 on 2024-07-21 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registerdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('password1', models.CharField(blank=True, max_length=100, null=True)),
                ('password2', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
