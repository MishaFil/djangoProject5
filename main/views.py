
from django.shortcuts import render
from .models import Product

def product_detail(request, product_id):
    product = Product.objects.get(pk=product_id)
    category_hierarchy = product.get_category_hierarchy()
    return render(request, 'product_detail.html', {'product': product, 'category_hierarchy': category_hierarchy})

def my_view(request):
    return render(request, 'index.html')