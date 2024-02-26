from django.urls import path
from cart.apps import CartConfig
from cart.views import (
    SuccessTemplateView,
    CanceledTemplateView,
    OrdersListView,
    ConfirmPayment,
)

app_name = CartConfig.name

urlpatterns = [
    path("order/", OrdersListView.as_view(), name="order"),
    path("confirm/", ConfirmPayment.as_view(), name="confirm"),
    path("order-success/", SuccessTemplateView.as_view(), name="order_success"),
    path("order_cancel/", CanceledTemplateView.as_view(), name="order_cancel"),
]
