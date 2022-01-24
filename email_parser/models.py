import datetime
import time

from django.db import models
#from djmoney.models.fields import MoneyField
#from moneyfield import MoneyField

class FutureClient(models.Model):
    # promo code add free trial
    # like for 30 days
    mail = models.CharField(max_length=50, primary_key=True, default='', blank=True)
    url = models.CharField(max_length=500, default='', blank=True)
    image = models.ImageField()




