from .models import *
from .views import *


def count(request):
    item_count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = CartList.objects.filter(cart_id=ca_id(request))
            cart_i = Items.objects.all().filter(cart=cart[:1])
            for c in cart_i:
                item_count += c.quantity
        except CartList.DoseNotExists:
            item_count = 0
        return dict(item_c=item_count)
