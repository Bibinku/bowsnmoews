# Generated by Django 5.0.6 on 2024-07-03 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Petend', '0003_breaddb_bdescription_categorydb_cbread'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breaddb',
            name='bage',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
