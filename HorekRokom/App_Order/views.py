from django.shortcuts import render, get_object_or_404,redirect

from django.contrib import messages
from django.contrib.auth.decorators import login_required

#models
from App_Order.models import Cart, Order
from App_Shop.models import Product
# Create your views here.

@login_required
def add_to_cart(request,pk):
    item=get_object_or_404(Product,pk=pk)
    order_item=Cart.objects.get_or_create(item=item,user=request.user,purchased=False)
    order_qs=Order.objects.filter(user=request.user)
    
    if order_qs.exists():
        order=order_qs[0]   #dictionary ke list kore
        if order.orderitems.filter(item=item).exists():
            order_item[0].quantity += 1
            order_item[0].save()
            messages.info(request,"This item quantity is updated.")
            return redirect("App_Shop:home")
        else:
            order.orderitems.add(order_item[0])
            messages.info(request,"This item is added to your Cart.")
            return redirect("App_Shop:home")
    else:
        order=Order(user=request.user)
        order.save()
        order.orderitems.add(order_item[0])
        messages.info(request,"This item is added to your Cart.")
        return redirect("App_Shop:home")


@login_required
def cart_view(request):
    carts=Cart.objects.filter(user=request.user,purchased=False)
    orders=Order.objects.filter(user=request.user,ordered=False)
    if carts.exists() and orders.exists():
        order=orders[0]
        return render(request,'App_Order/cart.htm',context={'carts':carts,'order':order})
    else:
        messages.warning(request,"You don't have any item in your Cart!")
        return redirect("App_Shop:home")


@login_required
def remove_from_cart(request,pk):
    item=get_object_or_404(Product,pk=pk)
    order_qs=Order.objects.filter(user=request.user,ordered=False)
    if order_qs.exists():
        order=order_qs[0]
        if order.orderitems.filter(item=item).exists():
            order_item=Cart.objects.filter(item=item,user=request.user,purchased=False)
            order_item=order_item[0]    #tuple object a convert hoy, easy to handle
            order.orderitems.remove(order_item)
            order_item.delete()
            messages.warning(request,"This item is removed from your cart")
            return redirect("App_Order:cart")
        else:
            messages.info(request,"This item wasn't in your Cart")
            return redirect("App_Shop:home")
    else:
        messages.info(request,"You don't have anything in your Cart.")
        return redirect("App_Shop:home")


@login_required
def increase_cart(request,pk):
    item=get_object_or_404(Product,pk=pk)
    order_qs=Order.objects.filter(user=request.user,ordered=False)

    if order_qs.exists():
        order=order_qs[0]
        if order.orderitems.filter(item=item).exists():
            order_item=Cart.objects.filter(item=item,user=request.user,purchased=False)[0]
            if order_item.quantity >= 1:
                order_item.quantity += 1
                order_item.save()
                messages.info(request,f"{item.name} quantity has been updated.")
                return redirect("App_Order:cart")
        else:
            messages.info(request,f"{item.name} is not in your Cart")
            return redirect("App_Shop:home") 
    else:
        messages.info(request,"You don't have an active order")
        return redirect("App_Shop:home")



@login_required
def decrease_cart(request,pk):
    item=get_object_or_404(Product,pk=pk)
    order_qs=Order.objects.filter(user=request.user,ordered=False)

    if order_qs.exists():
        order=order_qs[0]
        if order.orderitems.filter(item=item).exists():
            order_item=Cart.objects.filter(item=item,user=request.user,purchased=False)[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
                messages.info(request,f"{item.name} quantity has been updated.")
                return redirect("App_Order:cart")
            else:
                order.orderitems.remove(order_item)
                order_item.delete()
                messages.warning(request,f"{item.name} has been removed from Cart.")
                return redirect("App_Order:cart")
        else:
            messages.info(request,f"{item.name} is not in your Cart") 
            return redirect("App_Shop:home")
    else:
        messages.info(request,"You don't have an active order")
        return redirect("App_Shop:home")
