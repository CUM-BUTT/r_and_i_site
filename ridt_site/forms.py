import django.forms as forms

from ridt.models import Application, Price, PromoCode
from django.forms import Form, ImageField, ModelForm, CharField
from django import forms


class AppForm(ModelForm):
    image = ImageField()
    class Meta:
        model = Application
        fields = ['mail', 'url', 'name',
                  'app_id', 'promo_code', ]
        widgets = {
            'mail': forms.TextInput(attrs={'placeholder': 'Введите адрес Вашей электронной почты.', 'value': 'cum_butt@mail.ru', }),
            'url': forms.TextInput(attrs={'placeholder': 'Введите ссылку на Вашего сайт.', 'value': 'https://www.youtube.com/', }),
            'name': forms.TextInput(attrs={'placeholder': 'Введите имя Вашего приложения. Например: randi', 'value': 'randi_app', }),
            'app_id': forms.TextInput(attrs={'placeholder': 'Введите идентификатор Вашего приложения. Например: r_and_i_id', 'value': 'randi_id', }),
            'promo_code': forms.TextInput(attrs={'placeholder': 'Введите промокод, если он у Вас есть, или оставьте это поле пустым', 'value': '1488', }),
            'image': forms.TextInput(attrs={'placeholder': 'Введите промокод, если он у Вас есть, или оставьте это поле пустым', 'enctype': 'multipart/form-data', }),
        }

    def SetPrice(self):
        self.price = forms.DecimalField()
        price = Price.objects.get(currency='RU')
        self.price.prepare_value(price.price)

    def save(self, commit=True):
        self.SetPromoCode()
        self.SetPrice()

        super().save(commit=commit)
