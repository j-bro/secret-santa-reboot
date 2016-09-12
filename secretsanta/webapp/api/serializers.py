from django.contrib.auth.models import User
from rest_framework import serializers

from webapp.models import Exchange, PersonGroup


class ExchangeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exchange
        fields = ('name', 'description', 'group', 'created', 'modified', 'end_date', 'activated_date', 'price_cap', 'gift_lists')


class PersonGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = PersonGroup
        fields = ('name', 'manager', 'members',)


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
