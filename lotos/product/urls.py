from django.conf.urls import url
from .views import (
    ProductsListView, DiscountsListView
)

urlpatterns = [
    url(r'^discounts/$', DiscountsListView.as_view(), name='discounts'),
    url(r'^$', ProductsListView.as_view(), name='list'),
]
