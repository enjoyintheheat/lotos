from django.contrib.auth.mixins import (
    LoginRequiredMixin
)
from django.shortcuts import render, redirect, reverse
from django.views.generic.base import (
    TemplateView, View
)
from .models import Product

class ProductsListView(TemplateView):
    template_name = 'product.html'

    def get_context_data(self, **kwargs):
        context = super(ProductsListView, self).get_context_data(**kwargs)
        context['goods'] = Product.objects.all()

        return context

class DiscountsListView(TemplateView):
    template_name = 'discount.html'

    def get_context_data(self, **kwargs):
        context = super(DiscountsListView, self).get_context_data(**kwargs)
        context['discounts'] = Product.objects.filter(
            percentage__lt=100
        )

        return context
