# Generated by Django 3.0.6 on 2020-05-30 07:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("dashboard", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="company",
            name="primary_contact",
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
