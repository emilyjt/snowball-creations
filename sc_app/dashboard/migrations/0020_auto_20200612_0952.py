# Generated by Django 3.0.7 on 2020-06-12 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0019_auto_20200612_0905"),
    ]

    operations = [
        migrations.AlterField(
            model_name="company",
            name="subscriptions",
            field=models.ManyToManyField(blank=True, to="dashboard.Subscription"),
        ),
    ]
