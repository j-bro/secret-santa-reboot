from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic

from webapp.models import PersonGroup


@method_decorator(login_required, name='dispatch')
class GroupListView(generic.ListView):
    template_name = 'webapp/persongroup_list.html'
    context_object_name = 'user_groups'

    def get_queryset(self):
        """Return all groups which the user is part of."""
        return PersonGroup.objects.filter(members=self.request.user)


@method_decorator(login_required, name='dispatch')
class GroupDetailView(generic.DetailView):
    model = PersonGroup
    template_name = 'webapp/persongroup_detail.html'


class GroupCreateView(generic.CreateView):
    model = PersonGroup
    template_name = 'webapp/persongroup_create.html'
    fields = ['name', 'manager', 'members']


class GroupUpdateView(generic.UpdateView):
    model = PersonGroup
    fields = ['name', 'manager', 'members']


class GroupDeleteView(generic.DeleteView):
    model = PersonGroup
    success_url = reverse_lazy('group_list')
