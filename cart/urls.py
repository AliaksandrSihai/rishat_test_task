from django.urls import path
from cart.apps import CartConfig
from cart.views import (
    SuccessTemplateView,
    CanceledTemplateView,
    OrdersListView,
    CreateStripe,
)

app_name = CartConfig.name

urlpatterns = [
    path("order/", OrdersListView.as_view(), name="order"),
    path("create_stripe/<int:pk>", CreateStripe.as_view(), name="create_stripe"),
    path("order-success/", SuccessTemplateView.as_view(), name="order_success"),
    path("order_cancel/", CanceledTemplateView.as_view(), name="order_cancel"),
]
