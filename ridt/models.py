import datetime
import time

from django.db import models
#from djmoney.models.fields import MoneyField
#from moneyfield import MoneyField

class PromoCode(models.Model):
    # promo code add free trial
    # like for 30 days
    value = models.CharField(max_length=6, primary_key=True, default='', blank=True)

    description = models.TextField()
    usage_count = models.IntegerField(default=1,)
    trial_period = models.DurationField(default=datetime.timedelta(days=1,))

class Price(models.Model):
    currency = models.CharField(max_length=4, default='RU')
    price = models.DecimalField(decimal_places=2, max_digits=8, default=200)

    class Meta:
        unique_together = (('currency', 'price'),)


class Application(models.Model):
    mail = models.EmailField(max_length=20,)
    creation_time = models.DateTimeField(default=datetime.datetime.now(),)

    url = models.URLField(max_length=500,)
    name = models.CharField(max_length=20,)
    app_id = models.CharField(max_length=20,)

    promo_code = models.ForeignKey(PromoCode, on_delete=models.DO_NOTHING,)

    price = models.DecimalField(decimal_places=2, max_digits=8, default=200)#models.ForeignKey(Price, on_delete=models.DO_NOTHING,)
    next_payment_date = models.DateTimeField(default=datetime.datetime.now(),)

    def IsTimeToPay(self):
        return self.next_payment_date > datetime.datetime.now()

    def Pay(self, day_count):
        self.next_payment_date = datetime.datetime.now() + datetime.timedelta(days=day_count)

    def PayMonth(self,):
        self.Pay(day_count=30)

    def PayYear(self,):
        self.Pay(day_count=365)

    class Meta:
        unique_together = (('creation_time', 'mail'),)



