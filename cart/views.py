from django.shortcuts import render, redirect, get_object_or_404
# from shop.models import *
from . models import *
from django.core.exceptions import ObjectDoesNotExist
# from django.contrib.sessions.middleware import SessionMiddleware

# Create your views here.


def ca_id(request):
    ct_id = request.session.session_key
    if not ct_id:
        ct_id = request.session.create

    return ct_id


def cart_view(request, total=0, count=0, ct_item=None):
    try:
        ct = CartList.objects.get(cart_id=ca_id(request))
        ct_item = Items.objects.filter(cart=ct, active=True)
        for i in ct_item:
            total += (i.item_product.price * i.quantity)
            count += i.quantity
    except ObjectDoesNotExist:
        pass
    return render(request, 'cart.html', {'ci': ct_item, 'total': total, 'count': count})


def add_cart(request, dish_id):
    add_dish = Dishes.objects.get(id=dish_id)
    try:
        cart_obt = CartList.objects.get(cart_id=ca_id(request))
    except CartList.DoesNotExist:
        cart_obt = CartList.objects.create(cart_id=ca_id(request))
        cart_obt.save()
    try:
        c_items = Items.objects.get(item_product=add_dish, cart=cart_obt)
        if c_items.quantity < c_items.item_product.stock:
            c_items.quantity += 1
        c_items.save()
    except Items.DoesNotExist:
        c_items = Items.objects.create(item_product=add_dish, quantity=1, cart=cart_obt)
        c_items.save()
    return redirect('CartDetails')


def min_cart(request, dish_id):
    ct = CartList.objects.get(cart_id=ca_id(request))
    dish = get_object_or_404(Dishes, id=dish_id)
    ca_item = Items.objects.get(item_product=dish, cart=ct)
    if ca_item.quantity > 1:
        ca_item.quantity -= 1
        ca_item.save()
    else:
        ca_item.delete()
    return redirect('CartDetails')


def del_cart(request, dish_id):
    ct = CartList.objects.get(cart_id=ca_id(request))
    dish = get_object_or_404(Dishes, id=dish_id)
    ca_item = Items.objects.get(item_product=dish, cart=ct)
    ca_item.delete()
    return redirect('CartDetails')
