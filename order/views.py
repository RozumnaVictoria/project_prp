from django.shortcuts import render, redirect
from cart.cart import Cart
from order.forms import OrderForm
from order.models import OrderProduct


def order_create(request):
    if not request.user.is_authenticated:
        return redirect('users:login')
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        order = form.save()
        mass = []
        for item in cart:
            text_product = str(item['name']) + ' - ' + str(item['quantity'])
            mass.append(text_product)
        mass_str = '; '.join(mass)
        OrderProduct.objects.create(
            order=order,
            product=mass_str,
            price=cart.get_total_price(),
        )
        cart.clear()
        return redirect('order:order_done')
    else:
        form = OrderForm(request.POST)
    return render(request, 'order.html', {'form': form,
                                                'cart': cart,
                                                'get_total_price': cart.get_total_price()})


def done(request):
    if not request.user.is_authenticated:
        return redirect('users:login')
    return render(request, 'order_done.html')
