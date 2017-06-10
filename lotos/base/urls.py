from django.conf.urls import url
from .views import (
    PageIndex, PageAbout
)

urlpatterns = [
    url(r'^$', PageIndex.as_view(), name='index'),
    url(r'^about/$', PageAbout.as_view(), name='about'),
]
