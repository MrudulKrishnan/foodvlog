from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='hm'),
    path('search/', views.dish_search, name='search'),
    path('reg/', views.register, name='register'),
    path('<slug:c_slug>/', views.home, name='Dish_Category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.dish_details, name='details'),
]
