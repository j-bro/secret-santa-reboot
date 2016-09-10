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
        gift_list_obj = GiftList.objects.all().first()
        # gift_list_obj = GiftList.objects.filter(exchange=object).filter(user=self.request.user).first()
        context['gift_list'] = json.dumps(gift_list_obj.list)
        # TODO fix non existant gift list
        return context


class ExchangeCreateView(generic.CreateView):
    pass