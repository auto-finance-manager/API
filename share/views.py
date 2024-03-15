from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView, FormView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ShareOwnershipForm, SlotsForm, UpdateShareOwnershipForm
from .models import ShareOwnershipModel


class MyShareView(TemplateView):

    template_name = 'my_shares.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_shares'] = ShareOwnershipModel.objects.all()
        return context


class AddShareView(LoginRequiredMixin, TemplateView):
    template_name = 'add_stock.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['share_form'] = ShareOwnershipForm()
        context['slots_form'] = SlotsForm()
        return context

    def post(self, request, *args, **kwargs):
        share_form = ShareOwnershipForm(request.POST)
        slots_form = SlotsForm(request.POST)
        if share_form.is_valid() and slots_form.is_valid():
            code = share_form.cleaned_data.get('code')
            if not ShareOwnershipModel.objects.filter(code=code).exists():
                share_owner = share_form.save(commit=False)
                slot = slots_form.save()
                share_owner.owner = request.user
                share_owner.save()
                share_owner.slots.add(slot)
                share_owner.save()

        return self.get(request, *args, **kwargs)


class UpdateShareView(LoginRequiredMixin, DetailView):
    model = ShareOwnershipModel
    template_name = 'update_stock.html'
    slug_field = 'share__code'

    def get_context_data(self, object, **kwargs):
        context = super().get_context_data(**kwargs)
        context['share_form'] = UpdateShareOwnershipForm(instance=object)
        context['slots_form'] = SlotsForm()
        context['slots'] = object.get_slots().all()
        return context

    def post(self, request, *args, **kwargs):
        slug = kwargs.get('slug')
        share_owner = ShareOwnershipModel.objects.get(share__code=slug)
        owner_form = UpdateShareOwnershipForm(request.POST, instance=share_owner)
        owner_form.is_valid()
        share_owner.tracking = owner_form.cleaned_data.get('tracking')
        slots_form = SlotsForm(request.POST)
        if slots_form.is_valid():
            if slots_form.cleaned_data.get('quantity') > 0:
                slot = slots_form.save()
                share_owner.owner = request.user
                share_owner.slots.add(slot)
                share_owner.save()
            return HttpResponseRedirect(reverse('update-share', kwargs={'slug': slug}))
        return self.get(request, *args, **kwargs)
