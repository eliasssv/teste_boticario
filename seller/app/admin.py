from django.contrib import admin
from .models import Seller, Order

## Models registration on /admin
admin.site.register(Seller)
admin.site.register(Order)