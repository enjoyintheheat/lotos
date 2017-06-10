from django.conf.urls import url
from .views import (
    DashboardIndexView, DashboardArticlesView
)

urlpatterns = [
    url(r'^$', DashboardIndexView.as_view(), name='index'),
    url(r'^articles/$', DashboardArticlesView.as_view(), name='articles'),
]
