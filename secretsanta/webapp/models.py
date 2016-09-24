import random
from datetime import date

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy


class PersonGroup(models.Model):
    """
    A group of users that can participate in an exchange.
    """
    name = models.CharField(max_length=80)
    manager = models.ForeignKey(User, null=False, related_name='manages')
    members = models.ManyToManyField(User, related_name='person_groups')

    def get_current_exchanges(self):
        return self.exchanges.filter(end_date__gt=date.today())

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('group_detail', kwargs={'pk': self.id})


class Exchange(models.Model):
    """
    An exchange in which a group participates
    Structured Property of a Group Model
    """
    name = models.CharField(max_length=80, null=False, blank=False)
    description = models.TextField(null=False, blank=True)
    group = models.ForeignKey(PersonGroup, null=False, related_name='exchanges')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    end_date = models.DateField(null=False)
    activated_date = models.DateField(null=True, blank=True)
    price_cap = models.IntegerField()

    def __str__(self):
        return 'Exchange {}'.format(self.name)

    def get_absolute_url(self):
        return reverse_lazy('exchange_detail', kwargs={'pk': self.id})

    def activate_exchange(self):
        self.create_draws()
        self.activated_date = date.today()
        self.save()
        # TODO send emails

    def create_draws(self):
        exchange_members = list(self.group.members.all())
        random.shuffle(exchange_members)
        shifted_list = list(exchange_members)
        shifted_list.append(shifted_list.pop(0))
        for index, from_member in enumerate(exchange_members):
            to_member = shifted_list[index]
            self._make_draw(from_member, to_member)

    def _make_draw(self, from_user, to_user):
        draw = Draw()
        draw.from_user = from_user
        draw.to_user = to_user
        draw.exchange = self
        draw.save()


class Draw(models.Model):
    """
    Representation of a participant who will gift to another.
    Mapping for who will gift to who.
    """
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='drawed')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='drawed_by')
    exchange = models.ForeignKey(Exchange, on_delete=models.CASCADE, null=False, related_name='draws')

    def __str__(self):

        return 'Draw by {} of {}'.format(get_user_full_name_or_username(self.from_user), get_user_full_name_or_username(self.to_user))


class GiftList(models.Model):
    """
    Gift lists for a participant in an exchange
    """
    user = models.ForeignKey(User, null=False, related_name='gift_lists')
    exchange = models.ForeignKey(Exchange, related_name='gift_lists')
    gift_list = models.TextField(null=False, default='')

    def __str__(self):
        user_repr = self.user.get_full_name()
        if not user_repr:
            user_repr = self.user.username

        return 'Gift list of {} for exchange {}'.format(user_repr, self.exchange)


# TODO find a better place for this
def get_user_full_name_or_username(user):
    return user.get_full_name() if user.get_full_name() else user.username
