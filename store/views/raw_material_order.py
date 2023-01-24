from django.contrib.auth.hashers import  check_password
from django.views import View
from django.shortcuts import render, redirect
from icecream import ic
import json
from store.models.raw_material import Raw_material
from icecream import ic
import json
from store.models.customer import Customer
from store.models.orders import Order

class raw_material_order(View):
    def get(self,request):
        return render(request,"shef to vendor.html")
    def post(self, request):
        if request.method == "POST":
            if request.POST.get('b_sent'):
                return render(request,'shef wait.html')
    
        a = json.loads(request.body)['itemList']
        count1 = 0
        for i in a:
            k1,v1 = i.popitem()
            k2,v2 = i.popitem()
            k3,v3 = i.popitem()
        b = Raw_material(item= v2,quantity=v1)
        b.save()
        if request.method == "POST":
            if request.POST.get('b_sent'):
                return render(request,'shef wait.html')
        return render(request,'shef to vendor.html')

def new(request,items):
    return render(request,'shef wait.html',{'items':items})

def select(request):
    customers = Customer.objects.all()
    context = {'customers': customers}
    ic(customers)
    if request.method == "POST":
        name = list(request.POST.keys())[1]
        ic(name)
        #ic(name.split())
        if name:
            return redirect('shef',name)
    return render(request, 'customers2.html', context)



def shef(request,name):
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
        return redirect('raw_material_order')

    return render(request,'catering manager2.html',{'orders':orders,'item':item})

def vendor(request):
    # customers = Raw_material.objects.all()
    # context = {'customers': customers}
    # ic(customers)
    # if request.method == "POST":
    #     name = list(request.POST.keys())[1]
    #     ic(name)
    #     #ic(name.split())
    #     if name:
    return redirect('vendor2')
    # return render(request, 'customers.html', context)

def vendor2(request):
    customers = Raw_material.objects.all()
    ic(customers)
    if request.method == "POST":
        return redirect('vendor3')

    return render(request, 'catering manager3.html', {'customers': customers})






        
