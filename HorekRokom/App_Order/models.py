from django.db import models
from django.conf import settings
#Model
from App_Shop.models import Product

# Create your models here.

# didn't paid
class Cart(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name="cart")
    item=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    purchased=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True) #first bar
    updated=models.DateTimeField(auto_now=True)     #prottek update a

    def __str__(self):
        return f'(self.quantity) X (self.item)'
    
    def get_total(self):
        total=self.item.price*self.quantity
        float_total=format(total,'0.2f')
        return float_total


# paid cart items means order

class Order(models.Model):
    orderitems=models.ManyToManyField(Cart)
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    oredered=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    paymentID=models.CharField(max_length=264,blank=True,null=True)
    orderID=models.CharField(max_length=200,blank=True,null=True)

    def get_totals(self):
        total=0
        for order_item in self.orderitems.all():
            total+= float(oreder_item.get_total())
        return total 








    