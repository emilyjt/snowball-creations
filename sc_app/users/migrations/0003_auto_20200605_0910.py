# Generated by Django 3.0.6 on 2020-06-05 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_userprofile_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="image",
            field=models.ImageField(
                default="profile_pics/default.jpg", upload_to="profile_pics"
            ),
        ),
    ]
