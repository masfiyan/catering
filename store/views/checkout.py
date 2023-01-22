from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View

from store.models.product import Product
from store.models.orders import Order
from icecream import ic 


class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        date = request.POST.get('date')
        time = request.POST.get('time')
        total = request.POST.get('total')
        advance = request.POST.get('advance')
        remaining = request.POST.get('remaining')
        products = Product.get_products_by_id(list(cart.keys()))
        # ic(price,"p")
        # ic(quantity,"q")
        # print(advance,remaining, total,"heooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo")
        # total = list(total)
        #total = list(total)
        # remaining = list(remaining)
        # advance = list(advance)
        for product in products:
            print(cart.get(str(product.id) * product.price))
            order = Order(customer=Customer(id=customer),
                          product=product,
                          price=product.price,
                          address=address,
                          phone=phone,
                          d_date=date,
                          d_time=time,
                        #   advance=advance,
                        #   remaining=remaining,
                        #   total=total,
                          quantity=cart.get(str(product.id)))
            order.save()
        request.session['cart'] = {}
        if request.method == "POST":
            if request.POST.get('p_button'):
                return render(request,"a.html")

        return redirect('cart')
