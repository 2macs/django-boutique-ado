from django.shortcuts import render

# Create your views here.


def view_bag(request):
    """ Renders a view of the shopping bag """

    return render(request, 'bag/bag.html')
