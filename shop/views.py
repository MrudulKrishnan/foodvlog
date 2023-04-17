from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import *
from django.core.paginator import Paginator, EmptyPage, InvalidPage


# Create your views here.


def home(request, c_slug=None):
    # c_page = None
    # dishes_view = None

    if c_slug is not None:
        c_page = get_object_or_404(Category, slug=c_slug)
        dishes_view = Dishes.objects.filter(category=c_page, available=True)
    else:
        dishes_view = Dishes.objects.all().filter(available=True)
    category = Category.objects.all()
    paginator = Paginator(dishes_view, 4)
    try:
        page = int(request.GET.get('page', '1'))
    except():
        page = 1
    try:
        dish = paginator.page(page)
    except(EmptyPage, InvalidPage):
        dish = paginator.page(paginator.num_pages)

    return render(request, 'home_pr.html', {'dish': dishes_view, 'cate': category, 'page': dish})


def dish_details(request, c_slug, product_slug):
    try:
        dish = Dishes.objects.get(category__slug=c_slug, slug=product_slug)
    except Exception as e:
        raise e
    return render(request, 'item.html', {'dis': dish})


def dish_search(request):
    print('this is from dish')
    dish_s = None
    query = None
    if 'qu' in request.GET:
        query = request.GET.get('qu')
        dish_s = Dishes.objects.all().filter(Q(name__contains=query) | Q(desc__contains=query))
        print('this is from dish')
        print(query)
    return render(request, 'search.html', {'query': query, 'dish_s': dish_s})


def register(request):
    return render(request, 'registration.html')

