# Generated by Django 3.2.3 on 2021-05-31 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacts',
            name='instagram',
        ),
        migrations.RemoveField(
            model_name='contacts',
            name='telegram',
        ),
    ]