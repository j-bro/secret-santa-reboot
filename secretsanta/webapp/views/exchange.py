import json

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from django.http import HttpResponse

from webapp.models import Exchange, GiftList, Draw


@method_decorator(login_required, name='dispatch')
class ExchangeDetailView(generic.DetailView):
    model = Exchange
    template_name = 'webapp/exchange_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ExchangeDetailView, self).get_context_data(**kwargs)

        if self.object.group.manager == self.request.user:
            context['exchange_editable'] = True

        drawn_member = Draw.objects.filter(exchange=self.object, from_user=self.request.user).first().to_user
        if drawn_member:
            context['drawn_member'] = drawn_member

        member_gift_list_obj = GiftList.objects.filter(exchange=self.object, user=self.request.user).first()
        if member_gift_list_obj:
            context['member_gift_list'] = json.dumps(member_gift_list_obj.gift_list)

        drawn_member_gift_list_obj = GiftList.objects.filter(exchange=self.object, user=drawn_member).first()
        if drawn_member_gift_list_obj:
            context['drawn_member_gift_list'] = json.dumps(drawn_member_gift_list_obj.gift_list)

        return context


@method_decorator(login_required, name='dispatch')
class ExchangeCreateView(generic.CreateView):
    model = Exchange
    template_name = 'webapp/exchange_create.html'
    fields = ['name', 'description', 'group', 'end_date', 'price_cap']


@method_decorator(login_required, name='dispatch')
class ExchangeUpdateView(generic.UpdateView):
    model = Exchange
    fields = ['name', 'description', 'end_date', 'price_cap']


@method_decorator(login_required, name='dispatch')
class ExchangeDeleteView(generic.DeleteView):
    model = Exchange
    success_url = reverse_lazy('home')


@method_decorator(login_required, name='dispatch')
class ExchangeActivateView(generic.View):

    def get(self, request, pk):
        model = get_object_or_404(Exchange, pk=pk)
        model.activate_exchange()
        return redirect(model)


@method_decorator(login_required, name='dispatch')
class GiftListView(generic.View):

    def get(self, request, pk, user_id):
        model = get_object_or_404(GiftList, exchange=pk, user=user_id)
        return HttpResponse(model.gift_list, content_type="application/json")

    def post(self, request, pk, user_id):
        model, created = GiftList.objects.get_or_create(exchange=pk, user=user_id)
        post_list = request.POST.get('gift_list', None)
        model.gift_list = post_list
        status = 201 if created else 200
        return HttpResponse(status=status)

    def delete(self, request, pk, user_id):
        model = get_object_or_404(GiftList, exchange=pk, user=user_id)
        model.delete()
        # TODO return success