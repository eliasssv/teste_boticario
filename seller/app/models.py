from django.db import models
from .enums import OrderStatus
from django.utils import timezone

class Seller(models.Model):
    """
    Model of Seller
    \n@since 2020-08-21
    \n@author eliasssv
    """
    fullname = models.CharField(max_length=255, unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.fullname

class Order(models.Model):
    """
    Model of Order
    \n@since 2020-08-21
    \n@author eliasssv
    """
    code = models.IntegerField
    value = models.FloatField
    status = models.IntegerField(choices=OrderStatus.choices())
    date = models.DateField
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.code