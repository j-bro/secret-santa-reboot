import json

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views import generic

from webapp.models import Exchange, GiftList


@method_decorator(login_required, name='dispatch')
class ExchangeDetailView(generic.DetailView):
    model = Exchange
    template_name = 'webapp/exchange_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ExchangeDetailView, self).get_context_data(**kwargs)

        if self.object.group.manager == self.request.user:
            context['exchange_editable'] = True

        # TODO filter not working
        gift_list_obj = GiftList.objects.filter(exchange=self.object, user=self.request.user).first()
        context['gift_list'] = json.dumps(gift_list_obj.gift_list)
        # TODO fix if gift list doesn't exist
        return context


class ExchangeCreateView(generic.CreateView):
    pass