from rest_framework import generics, viewsets

from cart.models import Order
from cart.serializers import CartSerializer
from shop.models import Item
from shop.serializers import ItemSerializer


class ItemViewSet(viewsets.ModelViewSet):
    """Вьюсет для товара"""

    serializer_class = ItemSerializer
    queryset = Item.objects.all()


class CartRetrieveAPIView(generics.RetrieveAPIView):
    """Вьюсет для корзины"""

    serializer_class = CartSerializer
    queryset = Order.objects.all()


class CartListAPIView(generics.ListAPIView):
    """Вьюсет для корзин"""

    serializer_class = CartSerializer
    queryset = Order.objects.all()

    def get_queryset(self):
        if self.request.user.is_authenticated:
            queryset = Order.objects.all()
            return queryset