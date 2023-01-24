from django.db import models
from .product import Product
from .customer import Customer
import datetime
from django.utils import timezone
from datetime import date


class vendor(models.Model):

    item = models.TextField(default="")
    quantity = models.IntegerField(default=1)
    price = models.IntegerField(default=0)
    # def __str__(self):
    #     return str(self.id1)
    # @staticmethod
    # def get_orders_by_customer(customer_id):
    #     return Raw_material.objects.filter(item=customer_id).order_by('-date')