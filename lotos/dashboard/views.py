from django.core.paginator import Paginator
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import (
    LoginRequiredMixin, PermissionRequiredMixin
)
from django.shortcuts import render
from django.views.generic.base import TemplateView
from article.models import Article
from product.models import Product, WishlistTransaction
import arrow

class DashboardIndexView(LoginRequiredMixin, TemplateView):
    login_url = '/'
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardIndexView, self).get_context_data(**kwargs)
        context['reg_stats'] = self.get_reg_stats()
        context['article_stats'] = self.get_article_stats()
        context['sales_stats'] = self.get_sales_stats()
        context['category_ratio'] = self.get_category_ratio()

        return context

    def get_reg_stats(self):
        result_data = []
        User = get_user_model()
        date = arrow.now()
        for day in range(1, 30):
            count = User.objects.filter(
                created_at__gte=date.floor('day').datetime,
                created_at__lte=date.ceil('day').datetime
            ).count()
            date = date.replace(days=-1)
            result_data.append(count)

        return result_data

    def get_article_stats(self):
        result_data = []
        date = arrow.now()
        for day in range(1, 30):
            count = Article.objects.filter(
                date__gte=date.floor('day').datetime,
                date__lte=date.ceil('day').datetime
            ).count()
            date = date.replace(days=-1)
            result_data.append(count)

        return result_data

    def get_sales_stats(self):
        result_data = []
        date = arrow.now()
        for day in range(1, 30):
            count = WishlistTransaction.objects.filter(
                date__gte=date.floor('day').datetime,
                date__lte=date.ceil('day').datetime
            ).count()
            date = date.replace(days=-1)
            result_data.append(count)

        return result_data

    def get_category_ratio(self):
        result_data = []
        for item in ['овощи', 'фрукты', 'рыба', 'мясо', 'напитки', 'алкоголь']:
            result_data.append(
                Product.objects.filter(category=item).count()
            )

        return result_data

class DashboardArticlesView(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    login_url = '/'
    permission_required = (
        'articles.add_article',
        'articles.change_article',
        'articles.delete_article'
    )
    template_name = 'dashboard/article.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardArticlesView, self).get_context_data(**kwargs)
        articles_query = Article.objects.all()
        paginator = Paginator(articles_query, 10)
        articles = paginator.page(1)
        index = articles.number - 1
        max_index = len(paginator.page_range)
        start_index = index - 3 if index >= 3 else 0
        end_index = index + 3 if index <= max_index - 3 else max_index
        page_range = paginator.page_range[start_index:end_index]
        context['articles'] = articles
        context['page_range'] = page_range

        return context
