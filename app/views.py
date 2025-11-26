from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category, Comment
from django.http import JsonResponse
from .filter import filter_by
from .forms import OrderForm
from django.contrib import messages
from django.db.models import Avg

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
    comments = product.comments.filter(is_handle=False)[:4]
    related_products = Product.objects.filter(
    category=product.category
).exclude(id=product.id).order_by('-created_ad')[:4]
    context = {
        'product' : product,
        'comments' : comments,
        'related_products' : related_products
    }
    return render(request,'app/detail.html',context)





def order(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.product = product

            if order.quantity > product.stock:
                messages.error(request, 'Dont enough quantity')
            else:
                product.stock -= order.quantity
                product.save()
                order.save()

                messages.success(request, 'Order successfully sent ✅')

                return redirect('app:detail', product.id)

    else:
        form = OrderForm()

    context = {
        'form': form,
        'product': product,
    }

    return render(request, 'app/detail.html', context)




