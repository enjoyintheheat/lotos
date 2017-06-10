from django.contrib.auth.mixins import (
    LoginRequiredMixin
)
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic.base import (
    TemplateView, View
)
from product.models import Product, WishlistTransaction

class WishlistIndexView(TemplateView):
    template_name = "wishlist.html"

    def get_context_data(self, **kwargs):
        context = super(WishlistIndexView, self).get_context_data(**kwargs)
        context['goods'] = WishlistTransaction.objects.filter(
            user__email=self.request.user.email
        )

        return context

class WishlistAddView(LoginRequiredMixin, View):
    login_url = '/'

    def post(self, request):
        product_id = request.POST.get('pick_product', None)
        if product_id is None:
            return redirect(reverse('base:index'))
        product = get_object_or_404(Product, pk=product_id)
        m2m = WishlistTransaction(
            user=request.user,
            product=product
        )
        m2m.save()
        return redirect(reverse('wishlist:index'))

class WishlistDeleteView(LoginRequiredMixin, View):
    login_url = '/'

    def post(self, request):
        transaction_id = request.POST.get('drop_transaction', None)
        if transaction_id is None:
            return redirect(reverse('base:index'))
        transaction = get_object_or_404(WishlistTransaction, pk=transaction_id)
        transaction.delete()
        return redirect(reverse('wishlist:index'))
