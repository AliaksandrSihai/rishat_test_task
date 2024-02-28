from django.contrib import admin

from shop.models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    """Register post in admin-panel"""

    list_display = ("name", "description", "price", "currency")
    list_filter = ("name", "price")
    ordering = ("name",)

