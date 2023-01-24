from django.contrib.auth.hashers import  check_password
from django.views import View
from django.shortcuts import render, redirect
from icecream import ic
import json
from store.models.raw_material import Raw_material
from store.models.vendor import vendor
from icecream import ic
import json
from store.models.customer import Customer
from store.models.orders import Order
from django.http import QueryDict


class vendor3(View):
    def get(self,request):
        return render(request,"ven bill.html")
    def post(self,request): 
        if request.method == "POST":
            if request.POST.get('b_sent'):
                return render(request,'next.html')
    
        a = json.loads(request.body)['itemList']
        count1 = 0
        for i in a:
            k1,v1 = i.popitem()
            k2,v2 = i.popitem()
            k3,v3 = i.popitem()
            k4,v4 = i.popitem()
        b = vendor(item= v3,quantity=v2,price=v1)
        b.save()
        if request.method == "POST":
            if request.POST.get('b_sent'):
                return render(request,'next.html')
   
        return render(request,"ven bill.html")