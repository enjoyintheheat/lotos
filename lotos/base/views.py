from django.shortcuts import render
from django.views.generic.base import TemplateView
from account.forms import (
    LoginForm, UserCreationForm
)
from article.models import Article
from product.models import Product

class PageIndex(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(PageIndex, self).get_context_data(**kwargs)
        context['form'] = LoginForm
        context['form_reg'] = UserCreationForm
        context['articles'] = Article.objects.all()[:8]
        context['discounts'] = Product.objects.filter(
            percentage__lt=100
        ).order_by('?')[:5]

        return context

class PageAbout(TemplateView):
    template_name = 'about.html'
