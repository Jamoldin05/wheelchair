from django.shortcuts import render, redirect
from .models import Product, Category, Order
from django.http import JsonResponse
from .filter import filter_by
from .forms import OrderForm
# from django.http import HttpResponse




def home(request,category_id = None):
    categories = Category.objects.all()
    
    if category_id:
        products = Product.objects.filter(category = category_id)
    else:
        products = Product.objects.all()
        
    filter_by
    
    context = {
        'categories':categories,
        'products':products
    }
    return render(request,'app/home.html',context)



def detail(request,product_id):
    product = Product.objects.get(id = product_id)
    if not product_id:
        return JsonResponse(data={'massage': 'Ooops page not found (:','status_code':404})
    context = {
        'product' : product
    }
    return render(request,'app/detail.html',context)




def place_order(request):
    orders = Order.objects.all()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            product = order.product
            product.stock -= order.quantity
            product.save()
            order.save()
            return redirect('order_success') 
    else:
        form = OrderForm()

    context = {
        'form' : form
    }

    return render(request, 'app/detail.html', context)