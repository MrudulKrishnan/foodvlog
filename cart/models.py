from django.db import models
from shop.models import Dishes


# Create your models here.


class CartList(models.Model):
    DoseNotExists = None
    objects = None
    cart_id = models.CharField(max_length=100, default='default_cart_id')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cart_id


class Items(models.Model):
    objects = None
    item_product = models.ForeignKey(Dishes, on_delete=models.CASCADE)
    cart = models.ForeignKey(CartList, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.item_product

    def total(self):
        return self.item_product.price*self.quantity
