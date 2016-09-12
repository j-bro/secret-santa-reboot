from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from webapp.api import views


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'exchanges', views.ExchangeViewSet)
router.register(r'groups', views.PersonGroupViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^auth/', include('rest_framework.urls')),
    url(r'^', include(router.urls)),
]
