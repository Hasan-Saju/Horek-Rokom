from django import template
from App_Order.models import Order,Cart 

# template tag folder is for customized tags

register= template.Library()

@register.filter
def cart_total(user):
    cart=Cart.objects.filter(user=user,purchased=False)
    
    if cart.exists():
        return cart.count()
    else:
        return 0
