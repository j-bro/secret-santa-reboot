import json

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.urls import reverse_lazy

from webapp.models import Exchange, GiftList


@method_decorator(login_required, name='dispatch')
class ExchangeDetailView(generic.DetailView):
    model = Exchange
    template_name = 'webapp/exchange_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ExchangeDetailView, self).get_context_data(**kwargs)

        if self.object.group.manager == self.request.user:
            context['exchange_editable'] = True

        gift_list_obj = GiftList.objects.filter(exchange=self.object, user=self.request.user).first()
        if gift_list_obj:
            context['gift_list'] = json.dumps(gift_list_obj.gift_list)

        return context


class ExchangeCreateView(generic.CreateView):
    model = Exchange
    template_name = 'webapp/exchange_create.html'
    fields = ['name', 'description', 'group', 'end_date', 'price_cap']


class ExchangeUpdateView(generic.UpdateView):
    model = Exchange
    fields = ['name', 'description', 'end_date', 'price_cap']


class ExchangeDeleteView(generic.DeleteView):
    model = Exchange
    success_url = reverse_lazy('home')


class ExchangeActivateView(generic.View):

    def get(self):
        pass
