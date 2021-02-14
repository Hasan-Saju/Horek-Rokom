from django.shortcuts import render

# import views
from django.views.generic import ListView, DetailView

#Models
from App_Shop.models import Product,Category

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

def View_Category(request):
    # model=Category
    # context_object_name="category"
    # template_name='App_Shop/category.htm'
    category=Category.objects.all()
    print(category)
    print("hi")
    dict={"category":category}
    return render(request,"App_Shop/category.htm",context=dict)

def ProductDetail_from_Category(request,pk):
    # print("hello")
    products=Product.objects.filter(category=pk)
    # print("hi")
    # print(products)
    categoryName=Category.objects.get(pk=pk)
    # print()
    dict={"object_list":products,"category":"fromCategory","name":str(categoryName)}
    return render(request,"App_Shop/home.htm",context=dict)

    