from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.


class PersonGroup(Group):
    """
    A group of users that can participate in an exchange.
    """
    manager = models.ForeignKey(User, null=False)


class Exchange(models.Model):
    """
    An exchange in which a group participates
    Structured Property of a Group Model
    """
    name = models.CharField(max_length=80, null=False, blank=False)
    group = models.ForeignKey(PersonGroup, null=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    end_date = models.DateField(null=False)
    active = models.BooleanField(null=False, default=False)
    price_cap = models.IntegerField()

    def __str__(self):
        return 'Exchange {}'.format(self.name)


class Draw(models.Model):
    """
    Representation of a participant who will gift to another.
    Mapping for who will gift to who.
    """
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='from_user')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='to_user')
    exchange = models.ForeignKey(Exchange, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return 'Draw by {} of {}'.format(self.from_user.get_full_name(), self.to_user.get_full_name())


class GiftList(models.Model):
    """
    Gift lists for a participant in an exchange
    """
    user = models.ForeignKey(User,null=False)
    exchange = models.ForeignKey(Exchange, )
    list = models.TextField(null=False, default='')

    def __str__(self):
        return 'Gift list of {}'.format(self.user.get_full_name())
