# Generated by Django 3.0.6 on 2020-06-03 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_auto_20200603_0552'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscription',
            options={'ordering': ['social_profile', 'service_used']},
        ),
    ]
