from django.contrib import admin
# Register your models here.
from email_parser.models import FutureClient
from .models import *

admin.site.register(Application)
admin.site.register(Price)
admin.site.register(PromoCode)
admin.site.register(FutureClient)