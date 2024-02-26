import stripe
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views import generic, View
from django.views.generic import TemplateView

from cart.forms import CartForm
from cart.models import Order
from cart.service import create_payment
from django.views.decorators.csrf import csrf_exempt
from http import HTTPStatus
from django.http import HttpResponse, HttpResponseRedirect
from config.settings import DOMAIN_NAME, STRIPE_WEBHOOK_KEY


class SuccessTemplateView(TemplateView):
    template_name = "cart/success_order.html"
    title = " Спасибо за заказ!"


class OrderTemplateView(TemplateView):
    template_name = "cart/order_form.html"


class CanceledTemplateView(TemplateView):
    template_name = "cart/canceled.html"


class OrdersListView(generic.ListView):
    """Просмотр заказов"""

    model = Order
    form_class = CartForm
    success_url = reverse_lazy("/")

    template_name = "cart/cart_list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = Order.objects.select_related("product").filter(
            user=self.request.user, status=False
        )

        if cart.exists():
            context["object_list"] = cart
        return context


class ConfirmPayment(generic.CreateView):
    model = Order
    form_class = CartForm
    success_url = reverse_lazy("/")

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        price = request.POST.get('stripe_price_id')
        quantity = request.POST.get('quantity')
        session = stripe.checkout.Session.create(
            success_url=DOMAIN_NAME + reverse("cart:order_success"),
            line_items=[{"price": price, "quantity": quantity}],
            mode="payment",
            metadata={"payment_id": request.POST.get('id')},
        )
        return HttpResponseRedirect(session.url, status=HTTPStatus.SEE_OTHER)

@csrf_exempt
def stripe_webhook_view(request):
    payload = request.body
    sig_header = request.META["HTTP_STRIPE_SIGNATURE"]
    event = None
    try:
        event = stripe.Webhook.construct_event(payload, sig_header, STRIPE_WEBHOOK_KEY)
    except ValueError:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError:
        return HttpResponse(status=400)
    if event["type"] == "checkout.session.completed":
        session = stripe.checkout.Session.retrieve(event["data"]["object"]["id"])
        fulfill_order(session)

    return HttpResponse(status=200)


def fulfill_order(session):
    payment_id = int(session.metadata.payment_id)
    payment = Order.objects.get(pk=payment_id)
    payment.status = True
    payment.stripe_id = session.stripe_id
    payment.save()

