from django.conf.urls import url
from .views import (
    ArticleArchiveView, ArticleControlView, ArticlePageView
)

urlpatterns = [
    url(r'^$', ArticleArchiveView.as_view(), name='archive'),
    url(r'^control/$', ArticleControlView.as_view(), name='control'),
    url(r'^(?P<pk>\d+)$', ArticlePageView.as_view(), name='page')
]
