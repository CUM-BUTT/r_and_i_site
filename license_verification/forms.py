import django.forms as forms
from ridt.models import Application, Price, PromoCode
from django.forms import Form, ImageField, ModelForm
from ridt import models

class AppForm(ModelForm):
    class Meta:
        model = models.Application
        fields = '__all__'

