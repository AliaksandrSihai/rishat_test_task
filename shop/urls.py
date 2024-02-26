from shop.apps import ShopConfig
from django.urls import path

from shop.views import ListItem, RetrieveItem, BuyItemView

app_name = ShopConfig.name

urlpatterns = [
    path("", ListItem.as_view(), name="items"),
    path("item/<int:pk>", RetrieveItem.as_view(), name="item_details"),
    path("buy/<int:pk>", BuyItemView.as_view(), name="buy_item"),
]
