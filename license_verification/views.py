from django.shortcuts import render
# Create your views here.
from django.views.generic import TemplateView
from license_verification.forms import AppForm
from ridt.models import Application


class StatusView(TemplateView):
    template_name = 'main/app_status.html'

    def get_context_data(self, **kwargs):
        context = super(StatusView, self).get_context_data(**kwargs)
        user_site = self.request.GET.get('user_site', '')
        app = Application.objects.get(url=user_site)
        current_host = self.request.get_host()

        context.update({'next_payment_date': app.next_payment_date,
                        'validation_service': f'{current_host}/verification',
                        'block_banner': f'{current_host}/block_banner'},)

        return context

class BlockBannerView(TemplateView):
    template_name = 'main/block_banner.html'

