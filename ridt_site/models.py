import datetime

from django.db import models
#from moneyfield import MoneyField

class PromoCode(models.Model):
    # promo code add free trial
    # like for 30 days
    value = models.CharField(max_length=20, primary_key=True)

    description = models.TextField()
    usage_count = models.DecimalField(decimal_places=2, max_digits=8, default=1)
    trial_period = models.DecimalField(decimal_places=2, max_digits=8, default=30)

class Price(models.Model):
    currency = models.CharField(max_length=4, default='RU')
    price = models.DecimalField(decimal_places=2, max_digits=8, default=200)

    class Meta:
        unique_together = (('currency', 'price'),)

class Application(models.Model):
    creation_time = models.DateTimeField(default=datetime.datetime.now())
    mail = models.EmailField(max_length=20,)

    url = models.CharField(max_length=500)
    name = models.CharField(max_length=20)
    app_id = models.CharField(max_length=20)

    next_payment_date = models.DateField(primary_key=True, default=datetime.date.today())

    promo_code = models.ForeignKey(PromoCode, default=None, on_delete=models.DO_NOTHING)
    price = models.ForeignKey(Price, default=None, on_delete=models.DO_NOTHING)

    class Meta:
        unique_together = (('creation_time', 'mail'),)



