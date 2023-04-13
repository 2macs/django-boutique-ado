from django.shortcuts import render, redirect

# Create your views here.


def view_bag(request):
    """ Renders a view of the shopping bag """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """add a qty of an item to the bag"""

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})  # a session allows the user to add
    # to the bag until browser is closed,if nothing in bag empty dict created

    if item_id in list(bag.keys()):  # item already in the bag, increment it
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag  # update variable with new version
    return redirect(redirect_url)
