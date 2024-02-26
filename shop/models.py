from django.db import models
from users.models import NULLABLE


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

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"
