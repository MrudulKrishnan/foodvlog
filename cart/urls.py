from django.urls import path
from . import views

urlpatterns = [
    path('CartDetails/', views.cart_view, name='CartDetails'),
    path('Add/<int:dish_id>/', views.add_cart, name='AddCart'),
    path('min_cart/<int:dish_id>/', views.min_cart, name='CartDec'),
    path('del_cart/<int:dish_id>/', views.del_cart, name='CartDel'),
]
