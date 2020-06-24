# Generated by Django 3.0.6 on 2020-06-05 09:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0018_auto_20200604_0623"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("users", "0003_auto_20200605_0910"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="company",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="dashboard.Company",
            ),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="user",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
