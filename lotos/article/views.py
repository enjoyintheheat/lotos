from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.dates import ArchiveIndexView
from .forms import ArticleForm
from .models import Article

class ArticleControlView(TemplateView):
    template_name = 'article/control.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleControlView, self).get_context_data(**kwargs)
        context['article_form'] = ArticleForm()

        return context

class ArticleArchiveView(ArchiveIndexView):
    model = Article
    date_field = 'date'
    template_name = 'article/archive.html'

class ArticlePageView(TemplateView):
    template_name = 'article.html'

    def get_context_data(self, **kwargs):
        context = super(ArticlePageView, self).get_context_data(**kwargs)
        context['article'] = Article.objects.get(pk=kwargs['pk'])

        return context
