from django.conf.urls import url
from .views import (
    WishlistIndexView, WishlistAddView, WishlistDeleteView
)

urlpatterns = [
    url(r'^$', WishlistIndexView.as_view(), name='index'),
    url(r'^add/$', WishlistAddView.as_view(), name='add'),
    url(r'^delete/$', WishlistDeleteView.as_view(), name='delete'),
]
