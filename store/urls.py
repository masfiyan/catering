from django.contrib import admin
from django.urls import path
from .views.home import Index , store
from .views.signup import Signup
from .views.login import Login , logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
from .middlewares.auth import  auth_middleware
from .views.raw_material_order import raw_material_order,new,select,shef,vendor,vendor2
from .views.vendor import vendor3
from .views.catering import customer,catering,sended,catering4


urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('store', store , name='store'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),
    path('cart', auth_middleware(Cart.as_view()) , name='cart'),
    path('check-out', CheckOut.as_view() , name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
    path('raw_material_order',raw_material_order.as_view(),name="raw_material_order"),
    path('select',select,name="select"),
    path('shef/<str:name>/',shef,name="shef"),
    path('shef to vendor/<str:items>/',new,name="shef_to_vendor"),
    path('customer',customer,name="customer"),
    path('catering/<str:name>/',catering,name="catering"),
    path('sended',sended,name="sended"),
    path('vendor',vendor,name="vendor"),
    path('vendor2',vendor2,name="vendor2"),
    path('vendor3',vendor3.as_view(),name="vendor3"),
    path('catering4',catering4,name="catering4"),   
]
