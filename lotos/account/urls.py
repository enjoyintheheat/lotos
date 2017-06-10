from django.conf.urls import url
from .views import (
    AccountSigninView, AccountLogoutView, AccountSignupView,
    AccountDetailView
)

urlpatterns = [
    url(r'^signin/$', AccountSigninView.as_view(), name='signin'),
    url(r'^logout/$', AccountLogoutView.as_view(), name='logout'),
    url(r'^signup/$', AccountSignupView.as_view(), name='signup'),
    url(
        r'^(?P<email>[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)$',
        AccountDetailView.as_view(), name='detail'
    )
]
