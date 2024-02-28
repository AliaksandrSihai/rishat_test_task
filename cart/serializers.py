from rest_framework import serializers

from cart.models import Order


class CartSerializer(serializers.ModelSerializer):
    """Сериалайзер для корзины"""

    total_price = serializers.SerializerMethodField(read_only=True)

    def get_total_price(self, instance):
        price = instance.product.price
        return price * instance.quantity

    class Meta:
        model = Order
        fields = "__all__"
