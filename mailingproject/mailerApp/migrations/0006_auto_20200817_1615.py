# Generated by Django 3.1 on 2020-08-17 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailerApp', '0005_newsletter_contents'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscriber',
            name='conf_num',
        ),
        migrations.RemoveField(
            model_name='subscriber',
            name='confirmed',
        ),
    ]
