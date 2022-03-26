from django.shortcuts import render
from django.views.generic import TemplateView
from ridt_site.forms import AppForm


class Home(TemplateView):
    template_name = 'main/home.html'

class GoToBuilder(TemplateView):
    template_name = 'main/builder.html'
    http_method_names = ['get', 'post']

    def get_context_data(self, **kwargs):
        context = super(GoToBuilder, self).get_context_data(**kwargs)
        url = context['view'].request.GET.get('url', '')
        form = AppForm(initial={'url': url})
        context['form'] = form

        return context


class GoToSuccess(TemplateView):
    template_name = 'main/builder.html'
    http_method_names = ['get', 'post']

    def get_context_data(self, **kwargs):
        context = super(GoToSuccess, self).get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):
        form = AppForm(request.POST, request.FILES)
        if form.is_valid():
            pass
            form.RunBuildingSending(request)
            #form.SaveToDB()

        return render(request, 'main/success.html', {'form': form})


class NoPaymentView(TemplateView):
    template_name = 'main/block_banner.html'