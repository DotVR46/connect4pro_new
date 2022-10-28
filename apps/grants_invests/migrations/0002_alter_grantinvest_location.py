# Generated by Django 4.1.1 on 2022-10-28 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("grants_invests", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="grantinvest",
            name="location",
            field=models.CharField(
                blank=True,
                default="online",
                max_length=200,
                verbose_name="Место проведения",
            ),
        ),
    ]
