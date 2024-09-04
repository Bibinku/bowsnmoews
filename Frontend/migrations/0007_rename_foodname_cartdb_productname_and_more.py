# Generated by Django 5.0.6 on 2024-08-01 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0006_rename_username_cartdb_fusername'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartdb',
            old_name='foodname',
            new_name='productname',
        ),
        migrations.RenameField(
            model_name='cartdb',
            old_name='foodprice',
            new_name='quantity',
        ),
        migrations.RenameField(
            model_name='cartdb',
            old_name='fquantity',
            new_name='totalprice',
        ),
        migrations.RenameField(
            model_name='cartdb',
            old_name='fusername',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='cartdb',
            name='ftotalprice',
        ),
    ]
