from django import template

from cart.models import Order

register = template.Library()


@register.simple_tag
def total_amount(pk):
    model = Order.objects.get(pk=pk)
    price = model.product.price * model.quantity
    if model.discount is not None:
        discount = price * model.discount.percent / 100
        price -= discount

    if model.tax is not None:
        tax = price * model.tax.tax_percent / 100
        price += tax

    return price
