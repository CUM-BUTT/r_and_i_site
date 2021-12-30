import django.forms as forms

from ridt.models import Application, Price, PromoCode
from django.forms import Form, ImageField


class AppForm(Form):
    mail = forms.EmailField(label='mail', max_length=100)
    url = forms.URLField(label='url', max_length=1000)
    name = forms.CharField(label='name', max_length=100)
    app_id = forms.CharField(label='app_id', max_length=100)
    promo_code = forms.CharField(label='promo_code', max_length=8)
    photo = forms.ImageField(label='photo',)