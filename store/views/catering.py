from django.contrib.auth.hashers import  check_password
from django.views import View
from django.shortcuts import render, redirect
from icecream import ic
import json
from store.models.customer import Customer
from store.models.orders import Order


def customer(request):
    
    customers = Order.objects.all()
    context = {'customers': customers}
    ic(context)
    if request.method == "POST":
        name = list(request.POST.keys())[1]
        #ic(name.split())
        if name:
            return redirect('catering',name)
    return render(request, 'customers.html', context)

def catering(request,name):
   # name2 = name.split()
    #first = name2[0]
    #last = name2[1]
    customers = Order.objects.get(customer=1)
    ic(customers.product,customers.quantity,customers.phone,customers.address)
    name={'name':name,'phone':customers.phone,'date':customers.date,'time':customers.time,'email':customers.email}
    return render(request,'catering manager2.html',name)