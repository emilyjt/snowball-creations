# Generated by Django 3.0.6 on 2020-06-03 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0010_auto_20200603_0555"),
    ]

    operations = [
        migrations.AddField(
            model_name="subscription",
            name="name",
            field=models.CharField(max_length=200, null=True),
        ),
    ]
