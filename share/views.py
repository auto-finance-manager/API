from django.views.generic import TemplateView, FormView
from datetime import datetime, timedelta

from .forms import ShareOwnershipForm, SlotsForm
from .models import ShareOwnershipModel


class MyShareView(TemplateView):

    template_name = 'my_shares.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # timedelta(days=2)
        context['my_shares'] = ShareOwnershipModel.objects.all()
        return context

class AddShareView(TemplateView):
    template_name = 'add_stock.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['share_form'] = ShareOwnershipForm()
        context['slots_form'] = SlotsForm()
        return context
