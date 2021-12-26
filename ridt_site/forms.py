from .models import Application, Price
from django.forms import ModelForm


class AppForm(ModelForm):
    class Meta:
        model = Application