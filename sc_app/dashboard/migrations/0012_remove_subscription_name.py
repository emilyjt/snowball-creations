# Generated by Django 3.0.6 on 2020-06-03 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0011_subscription_name"),
    ]

    operations = [
        migrations.RemoveField(model_name="subscription", name="name",),
    ]
