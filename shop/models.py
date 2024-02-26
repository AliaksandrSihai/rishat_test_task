import stripe
from django.db import models

from config.settings import STRIPE_SECRET_KEY
from users.models import NULLABLE

stripe.api_key = STRIPE_SECRET_KEY


class Item(models.Model):
    """Модель для товара"""

    currency = {
        ("USD", "USD"),
        ("RUB", "RUB"),
    }
    name = models.CharField(max_length=255, verbose_name="название")
    description = models.TextField(verbose_name="описание", **NULLABLE)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="цена")
    currency = models.CharField(max_length=3, choices=currency, verbose_name="валюта")
    stripe_price_id = models.CharField(max_length=128, **NULLABLE)

    def __str__(self):
        return self.name

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if not self.stripe_price_id:
            stripe_product_price = self.product_create_stripe()
            self.stripe_price_id = stripe_product_price["id"]
        return super().save(
            force_insert=False, force_update=False, using=None, update_fields=None
        )

    def product_create_stripe(self):
        stripe_product = stripe.Product.create(name=self.name)

        stripe_product_price = stripe.Price.create(
            product=stripe_product["id"],
            currency=self.currency,
            unit_amount=round(self.price * 100),
        )
        return stripe_product_price

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"
