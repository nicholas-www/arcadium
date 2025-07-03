from django.shortcuts import render

from products.models import Product


# Create your views here.

def index(request):
    featured_products = Product.objects.all()

    context = {'featured_products': featured_products}
    return render(request, 'home/index.html', context)
