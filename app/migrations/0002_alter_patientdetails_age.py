# Generated by Django 4.2 on 2023-04-10 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientdetails',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
