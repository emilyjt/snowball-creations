# Generated by Django 3.0.6 on 2020-06-03 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0012_remove_subscription_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="service",
            name="details",
            field=models.TextField(max_length=1000, null=True),
        ),
    ]
