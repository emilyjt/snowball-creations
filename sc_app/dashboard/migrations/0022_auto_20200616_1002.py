# Generated by Django 3.0.7 on 2020-06-16 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0021_auto_20200614_1222"),
    ]

    operations = [
        migrations.AlterField(
            model_name="socialnetwork",
            name="logo",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="sc_app/static/media/socialnetworklogos",
            ),
        ),
    ]
