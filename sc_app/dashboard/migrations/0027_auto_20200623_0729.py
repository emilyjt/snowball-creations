# Generated by Django 3.0.7 on 2020-06-23 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0026_auto_20200619_1920'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='date_created',
        ),
        migrations.AlterField(
            model_name='subscription',
            name='service_used',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.Service'),
        ),
    ]
