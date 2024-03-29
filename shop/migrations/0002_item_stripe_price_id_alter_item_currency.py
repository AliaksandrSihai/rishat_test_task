# Generated by Django 4.2.7 on 2024-02-26 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="stripe_price_id",
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name="item",
            name="currency",
            field=models.CharField(
                choices=[("USD", "USD"), ("RUB", "RUB")],
                max_length=3,
                verbose_name="валюта",
            ),
        ),
    ]
