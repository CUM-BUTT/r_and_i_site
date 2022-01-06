from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from license_verification.forms import AppForm
from ridt.models import Application


class StatusView(TemplateView):
    template_name = 'main/app_status.html'

    def get_context_data(self, **kwargs):
        context = super(StatusView, self).get_context_data(**kwargs)
        app = Application.objects.get(name=context['name'])
        form = AppForm(instance=app)
        context['form'] = form

        return context