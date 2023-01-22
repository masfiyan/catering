from django.db import models
from .product import Product
from .customer import Customer
import datetime
from django.utils import timezone
from datetime import date


class Raw_material(models.Model):
    # product = models.ForeignKey(Product,
    #                             on_delete=models.CASCADE)
    # customer = models.ForeignKey(Customer,
    #                              on_delete=models.CASCADE)
    item = models.TextField()
    