from django.db.models import Q
from .models import Product
from django.shortcuts import render



def filter_by(request,filter_type):

    products = Product.objects.all()

    if filter_type == 'expensive':
        products = products.order_by('-price')
    elif filter_type == 'cheap':
        products = products.order_by('price')
    elif filter_type == 'sale':
        products = products.filter(discount__gt = 0).order_by('-discount')
    else:
        products = products.order_by('created_ad')

    context = {
        'products' : products
    }
    return render (request, 'app/home.html', context)




def search(request):
    q = request.GET.get('q','')
    if q:
        products = Product.objects.filter(
            Q(name__icontains = q) | Q(description__icontains = q)
        )
    else :
        products = Product.objects.all()

    context = {
        'q' : q,
        'products' : products
    }

    return render (request, 'app/home.html', context)