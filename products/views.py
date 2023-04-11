from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product


# Create your views here.
def all_products(request):
    """ A view to show all products including sorting and searching """

    products = Product.objects.all()
    query = None  # make page can page can load if a search term not provided.

    # if somebody uses search bar
    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, 'No search criteria entered!')
                return redirect(request('products'))

            # the pipe means OR, the i makes it case insensitive
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {'products': products,
               'search_term': query}
    return render(request, 'products/products.html', context)


# Create view for detailed product template
def product_detail(request, product_id):
    """ A view to show a specific product and associated details """

    product = get_object_or_404(Product, pk=product_id)
    context = {'product': product}
    return render(request, 'products/product_detail.html', context)
