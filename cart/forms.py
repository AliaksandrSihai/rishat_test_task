from django.forms import ModelForm

from cart.models import Order
from shop.forms import StyleFormMixin


class CartForm(StyleFormMixin, ModelForm):
    """Форма для корзины"""

    class Meta:
        model = Order
        fields = "__all__"
