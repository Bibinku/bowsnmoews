# Generated by Django 5.0.6 on 2024-07-25 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0003_bookslotdb'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookslotdb',
            old_name='age',
            new_name='Bage',
        ),
        migrations.RenameField(
            model_name='bookslotdb',
            old_name='bread',
            new_name='Bbread',
        ),
        migrations.RenameField(
            model_name='bookslotdb',
            old_name='date',
            new_name='Bdate',
        ),
        migrations.RenameField(
            model_name='bookslotdb',
            old_name='subject',
            new_name='Bmessage',
        ),
        migrations.RenameField(
            model_name='bookslotdb',
            old_name='name',
            new_name='Bname',
        ),
        migrations.RenameField(
            model_name='bookslotdb',
            old_name='number',
            new_name='Bnumber',
        ),
        migrations.RenameField(
            model_name='bookslotdb',
            old_name='services',
            new_name='Bservices',
        ),
        migrations.RenameField(
            model_name='bookslotdb',
            old_name='sex',
            new_name='Bsex',
        ),
        migrations.RenameField(
            model_name='bookslotdb',
            old_name='time',
            new_name='Btime',
        ),
    ]