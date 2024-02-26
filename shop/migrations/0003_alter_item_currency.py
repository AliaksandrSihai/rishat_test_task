# Generated by Django 4.2.7 on 2024-02-26 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0002_item_stripe_price_id_alter_item_currency"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="currency",
            field=models.CharField(
                choices=[("RUB", "RUB"), ("USD", "USD")],
                max_length=3,
                verbose_name="валюта",
            ),
        ),
    ]