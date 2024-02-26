import stripe
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views import generic, View
from django.views.generic import TemplateView
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

    template_name = "cart/order_form.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = Order.objects.select_related("product").filter(
            user=self.request.user, status=False
        )
        if cart.exists():
            context["object_list"] = cart
        return context


class CreateStripe(View):
    """Создание платежа в Stripe"""

    def post(self, request, pk):
        order = Order.objects.get(pk=pk)
        price = order.product.price * order.quantity

        if order.discount is not None:
            discount = price * order.discount.percent / 100
            price -= discount

        if order.tax is not None:
            tax = price * order.tax.tax_percent / 100
            price += tax
        try:
            stripe_id = create_payment(
                amount=price, currency=order.product.currency.lower()
            )
            order.stripe_id = stripe_id
            order.status = True
            order.save()
            return redirect("cart:order_success")
        except ValueError:
            return redirect("cart:order_cancel")


# class ConfirmPayment(generic.CreateView):
#     model = PaymentModel
#     template_name = "payments/confirm_payment.html"
#     form_class = PaymentForm
#     success_url = reverse_lazy("posts:all_posts")
#
#     def post(self, request, *args, **kwargs):
#         form = self.get_form()
#         payment_instance = Subscription.objects.get(pk=int(form.data["subscription"]))
#         super(ConfirmPayment, self).post(request, *args, **kwargs)
#         price = payment_instance.stripe_price_id
#         session = stripe.checkout.Session.create(
#             success_url=DOMAIN_NAME + reverse("payments:success"),
#             line_items=[{"price": price, "quantity": 1}],
#             mode="payment",
#             metadata={"payment_id": self.object.id},
#         )
#         return HttpResponseRedirect(session.url, status=HTTPStatus.SEE_OTHER)
#
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super(ConfirmPayment, self).form_valid(form)
#
#
# @csrf_exempt
# def stripe_webhook_view(request):
#     payload = request.body
#     sig_header = request.META["HTTP_STRIPE_SIGNATURE"]
#     event = None
#     try:
#         event = stripe.Webhook.construct_event(payload, sig_header, STRIPE_WEBHOOK_KEY)
#     except ValueError:
#         return HttpResponse(status=400)
#     except stripe.error.SignatureVerificationError:
#         return HttpResponse(status=400)
#     if event["type"] == "checkout.session.completed":
#         session = stripe.checkout.Session.retrieve(event["data"]["object"]["id"])
#
#         fulfill_order(session)
#
#     return HttpResponse(status=200)
#
#
# def fulfill_order(session):
#     payment_id = int(session.metadata.payment_id)
#     payment = PaymentModel.objects.get(pk=payment_id)
#     payment.payment_status = True
#     payment.stripe_id = session.stripe_id
#     payment.save()
#
#     user = User.objects.get(pk=payment.user.pk)
#     user.is_paid_subscribe = True
#     user.save()
