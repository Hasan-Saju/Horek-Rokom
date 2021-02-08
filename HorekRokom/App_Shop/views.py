from django.shortcuts import render

# import views
from django.views.generic import ListView, DetailView

#Models
from App_Shop.models import Product

# Mixin
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.



class Home(ListView):
    model=Product
    template_name='App_Shop/home.htm'


class ProductDetail(LoginRequiredMixin, DetailView):
    model=Product
    context_object_name="product"
    template_name='App_Shop/product_details.htm'