from django.contrib.auth.hashers import  check_password
from django.views import View
from django.shortcuts import render, redirect
from icecream import ic
import json
from store.models.raw_material import Raw_material

class raw_material_order(View):
    def get(self,request):
        return render(request,"shef to vendor.html")
    def post(self, request):
        if request.method == "POST":
            if request.POST.get('b_sent'):
                return render(request,'shef wait.html')
        items = Raw_material(item=json.loads(request.body)['itemList'])
        items.save()
        ic(items.item)
        if request.method == "POST":
            if request.POST.get('b_sent'):
                return render(request,'shef wait.html')
            # ic("heloooooooooooooooooooooooooooo")
            # return redirect('shef_to_vendor',items=items)
        return render(request,'shef to vendor.html')

def new(request,items):
    ic(13123234443335)
    return render(request,'shef wait.html',{'items':items})
        
