# Generated by Django 3.0.7 on 2020-06-19 19:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0025_company_created_at"),
    ]

    operations = [
        migrations.RemoveField(model_name="company", name="created_at",),
        migrations.AddField(
            model_name="company",
            name="date_created",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="date created"
            ),
        ),
    ]
