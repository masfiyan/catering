from django.db import models
from .product import Product
from .customer import Customer
import datetime
from django.utils import timezone
from datetime import date


class Order(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE)
    
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    d_date = models.DateField(default = date.today)
    d_time = models.TimeField(default = timezone.now)
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    # advance = models.IntegerField(default=0, null=True, blank=True)
    # remaining = models.IntegerField(default=0, null=True, blank=True)
    # total = models.IntegerField(default=0, null=True, blank=True)
    status = models.BooleanField(default=False)

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')

    # def __str__(self):
    #     return str(self.customer)

