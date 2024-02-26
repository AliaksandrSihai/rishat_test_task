from django.contrib import admin

from cart.models import Order, Discount, Tax

# Register your models here.
admin.site.register(Order)
admin.site.register(Discount)
admin.site.register(Tax)
