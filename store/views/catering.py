from django.contrib.auth.hashers import  check_password
from django.views import View
from django.shortcuts import render, redirect
from icecream import ic
import json
from store.models.customer import Customer
from store.models.orders import Order
from store.models.vendor import vendor


def customer(request):
    
    customers = Customer.objects.all()
    context = {'customers': customers}
    ic(customer)
    if request.method == "POST":
        if request.POST.get('vendor'):
            return redirect('catering4')
        name = list(request.POST.keys())[1]
        ic(name)
        #ic(name.split())
        if name:
            return redirect('catering',name)
         
    return render(request, 'customers.html', context)

def catering(request,name):

    customer = Order.objects.filter(customer=name)
    ic(customer)
    item = {}
    for i in customer:
        item['name'] = name
        item['phone'] = i.phone
        item['address'] = i.address
        item['date'] = i.date
        item['d_date'] = i.d_date
        item['d_time'] = i.d_time

    orders = Order.get_orders_by_customer(name)
    if request.method == "POST":
        return redirect('sended')

    return render(request,'catering manager2.html',{'orders':orders,'item':item})  

def sended(request):
    return render(request,'sent_chef.html')

def catering4(request):
    customer = vendor.objects.all()
    ic(customer)
    count = 0
    for i in customer:
        count = count + i.price
    ic(count)

    return render(request,'catering manager4.html',{'customer':customer,'price':count})
