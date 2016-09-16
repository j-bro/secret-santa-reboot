"""secretsanta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include

from webapp.views import main, group, auth, exchange

urlpatterns = [

    url(r'^how-it-works', main.how_it_works, name='how_it_works'),
    url(r'^signup', auth.signup_user, name='signup'),
    url(r'^home', main.home, name='home'),

    url(r'^', include('django.contrib.auth.urls')),

    url(r'^api/', include('webapp.api.urls')),

    url(r'^group/$', group.GroupListView.as_view(), name='group_list'),
    url(r'^group/create/$', group.GroupCreateView.as_view(), name='group_create'),
    url(r'^group/(?P<pk>[0-9]+)/$', group.GroupDetailView.as_view(), name='group_detail'),
    url(r'^group/(?P<pk>[0-9]+)/delete/$', group.GroupDeleteView.as_view(), name='group_delete'),

    url(r'^exchange/create/$', exchange.ExchangeCreateView.as_view(), name='exchange_create'),
    url(r'^exchange/(?P<pk>[0-9]+)/$', exchange.ExchangeDetailView.as_view(), name='exchange_detail'),
    url(r'^exchange/(?P<pk>[0-9]+)/delete/$', exchange.ExchangeDeleteView.as_view(), name='exchange_delete'),

    url(r'^$', main.index, name='index'),
]
