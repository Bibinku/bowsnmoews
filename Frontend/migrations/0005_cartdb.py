# Generated by Django 5.0.6 on 2024-07-31 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0004_rename_age_bookslotdb_bage_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('foodname', models.CharField(blank=True, max_length=100, null=True)),
                ('fquantity', models.IntegerField(blank=True, null=True)),
                ('foodprice', models.IntegerField(blank=True, null=True)),
                ('ftotalprice', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
