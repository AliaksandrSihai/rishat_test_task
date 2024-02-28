from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, redirect
from django.views import View, generic

from cart.forms import CartForm
from cart.models import Order
from shop.models import Item


class ListItem(generic.ListView):
    """Список Item'ов"""

    model = Item

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = Item.objects.all()
        return context


class RetrieveItem(generic.DetailView):
    """Получение конкретного обьекта"""

    model = Item
    form_class = CartForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        Formset = inlineformset_factory(Item, Order, form=CartForm, extra=1)
        context["formset"] = Formset(instance=self.object)
        context["object_list"] = Item.objects.filter(pk=self.object.pk)
        return context


class BuyItemView(View):
    """Добавление товара в корзину"""

    def post(self, request, pk):
        quantity_value = request.POST.get("quantity", "1")
        product = get_object_or_404(Item, pk=pk)
        Order.objects.create(
            product=product, quantity=int(quantity_value), user=self.request.user
        )
        return redirect("cart:order")
