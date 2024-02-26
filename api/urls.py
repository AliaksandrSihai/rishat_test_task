from django.urls import path
from rest_framework import routers

from api.apps import ApiConfig
from api.views import CartRetrieveAPIView, ItemViewSet, CartListAPIView

app_name = ApiConfig.name


router = routers.DefaultRouter()
router.register(r"item", ItemViewSet, basename="item")


urlpatterns = [
    path("cart/<int:pk>/", CartRetrieveAPIView.as_view(), name="cart"),
    path("all_carts/", CartListAPIView.as_view(), name="all_carts"),
] + router.urls
