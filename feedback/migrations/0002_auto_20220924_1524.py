# Generated by Django 3.2.15 on 2022-09-24 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='Description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='rate_us',
            new_name='rating',
        ),
    ]