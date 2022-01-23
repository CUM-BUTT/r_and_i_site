from datetime import datetime, timedelta

import csrf as csrf
import requests
import pickle as pk
from ridt.models import Application, Price, PromoCode
from django.forms import Form, ImageField, ModelForm, CharField
from django import forms
from django.template.context_processors import csrf
from django.http import HttpResponse, HttpResponseRedirect

class AppForm(Form):
    url = forms.CharField(max_length=1000,
                          widget=forms.TextInput(attrs={'placeholder': 'Введите адрес Вашей электронной почты.',
                                                        'value': 'https://www.youtube.com/', }))
    mail = forms.EmailField(widget=forms.TextInput(
        attrs={'placeholder': 'Введите адрес Вашей электронной почты.', 'value': 'cum_butt@mail.ru', }))

    name = forms.CharField(max_length=100,
                           widget=forms.TextInput(
                               attrs={'placeholder': 'Введите имя Вашего приложения. Например: randi',
                                      'value': 'randi_app', }))
    app_id = forms.CharField(max_length=100,
                             widget=forms.TextInput(
                                 attrs={'placeholder': 'Введите идентификатор вашего приложения. Например: randi_id',
                                        'value': 'randi_id', }))

    promo_code = forms.CharField(max_length=20, required=False,
                        widget=forms.TextInput(attrs={'placeholder': 'Введите промокод, если он у Вас есть, или оставьте это поле пустым', 'value': '1488', }))
    image = ImageField()

    def RunBuildingSending(self, request):
        url = request.build_absolute_uri('/')
        image = pk.dumps(self.cleaned_data['image'].file)
        del(self.cleaned_data['image'])

        requests.post(url=f'{url}builder/', data=self.cleaned_data, files={'image': image}, cookies=request.COOKIES)

    def SaveToDB(self):
        no_promo = 'no_promo'
        promo = []

        if hasattr(self, 'promo_code'):
            promo = PromoCode.objects.filter(value=self.promo_code)
        if len(promo) == 0:
            promo = PromoCode.objects.filter(value=no_promo)[0]

        price = Price.objects.filter(currency='RU')[0].price
        next_payment_date = datetime.now() + promo.trial_period

        model = Application(name=self.cleaned_data['name'], url=self.cleaned_data['url'],
                            mail=self.cleaned_data['mail'], app_id=self.cleaned_data['app_id'],
                            promo_code=promo, price=price, next_payment_date=next_payment_date)
        model.save()

