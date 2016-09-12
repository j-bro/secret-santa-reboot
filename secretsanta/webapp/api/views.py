from django.contrib.auth.models import User
from rest_framework import viewsets

from webapp.models import Exchange, PersonGroup
from webapp.api.serializers import ExchangeSerializer, UserSerializer, PersonGroupSerializer


class ExchangeViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Exchange.objects.all()
    serializer_class = ExchangeSerializer


class PersonGroupViewSet(viewsets.ModelViewSet):
    queryset = PersonGroup.objects.all()
    serializer_class = PersonGroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
        This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
