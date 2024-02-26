import stripe
from django.urls import reverse
from config.settings import STRIPE_SECRET_KEY

stripe.api_key = STRIPE_SECRET_KEY


def create_payment(amount, currency):
    """Создание платежа"""
    amount_stripe = int(amount * 100)
    secret = stripe.PaymentIntent.create(
        amount=amount_stripe,
        currency=currency,
        setup_future_usage="off_session",
        payment_method_types=["card"],
    )
    confirmation = stripe.PaymentIntent.confirm(
        secret.id,
        payment_method="pm_card_visa",
        return_url="http://localhost:8000" + reverse("cart:order"),
    )
    return secret.id
