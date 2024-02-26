# Generated by Django 4.2.7 on 2024-02-26 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cart", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="stripe_id",
            field=models.CharField(
                blank=True,
                max_length=128,
                null=True,
                verbose_name="id платежа на stripe",
            ),
        ),
    ]