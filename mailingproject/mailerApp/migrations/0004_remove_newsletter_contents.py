# Generated by Django 2.2.5 on 2020-08-16 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailerApp', '0003_newsletter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsletter',
            name='contents',
        ),
    ]
