from django.shortcuts import render

from products.models import Product


# Create your views here.
def product_details(request, product_id):
    product = Product.objects.get(id=product_id)
    related_products = Product.objects.all()

    context = {'product': product, 'related_products': related_products[:4]}
    return render(request, 'products/product-details.html', context)
