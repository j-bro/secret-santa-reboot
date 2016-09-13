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
from django.contrib.auth import views

from webapp.views import main, group, auth, exchange

urlpatterns = [
    url(r'^$', main.index, name='index'),
    url(r'^how-it-works', main.how_it_works, name='how_it_works'),
    # url(r'^login', auth.login_user, name='login'),
    # url(r'^logout', auth.logout_user, name='logout'),
    url(r'^signup', auth.signup_user, name='signup'),
    url(r'^home', main.home, name='home'),

    url(r'^login/$', views.login, {'template_name': 'webapp/registration/login.html'}, name='login'),
    url(r'^logout/$', views.logout, {'template_name': 'webapp/registration/logout.html'}, name='logout'),
    url(r'^password_change/$', views.password_change, {'template_name': 'webapp/registration/password_change_form.html'},
        name='password_change'),
    url(r'^password_change/done/$', views.password_change_done,
        {'template_name': 'webapp/registration/password_change_done.html'}, name='password_change_done'),
    url(r'^password_reset/$', views.password_reset, {'template_name': 'webapp/registration/password_reset.html'},
        name='password_reset'),
    url(r'^password_reset/done/$', views.password_reset_done,
        {'template_name': 'webapp/registration/password_reset_done.html'}, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.password_reset_confirm, {'template_name': 'webapp/registration/password_reset_confirm.html'}, name='password_reset_confirm'),
    url(r'^reset/done/$', views.password_reset_complete, {'template_name': 'webapp/registration/password_reset_complete.html'},
        name='password_reset_complete'),

    url(r'^api/', include('webapp.api.urls')),

    url(r'^group/$', group.GroupListView.as_view(), name='group_list'),
    url(r'^group/create/$', group.GroupCreateView.as_view(), name='group_create'),
    url(r'^group/(?P<pk>[0-9]+)/$', group.GroupDetailView.as_view(), name='group_detail'),

    url(r'^exchange/create/$', exchange.ExchangeCreateView.as_view(), name='exchange_create'),
    url(r'^exchange/(?P<pk>[0-9]+)/$', exchange.ExchangeDetailView.as_view(), name='exchange_detail'),
]
