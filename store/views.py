from django.shortcuts import redirect, get_object_or_404, render
from .models import Product
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


def home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'home.html', context)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart = request.session.get('cart', {})

    if str(pk) in cart:
        cart[str(pk)] += 1
    else:
        cart[str(pk)] = 1

    request.session['cart'] = cart
    return redirect('view_cart')

def view_cart(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0

    for product_id, quantity in cart.items():
        product = Product.objects.get(pk=product_id)
        item_total = product.price * quantity
        total += item_total
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'item_total': item_total,
        })

    context = {
        'cart_items': cart_items,
        'total': total
    }
    return render(request, 'cart.html', context)

@login_required  # requires user to be logged in
def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        return redirect('view_cart')  # nothing to checkout!

    order = Order.objects.create(user=request.user, complete=True)

    for product_id, quantity in cart.items():
        product = Product.objects.get(pk=product_id)
        OrderItem.objects.create(
            product=product,
            order=order,
            quantity=quantity
        )

    # clear the cart
    request.session['cart'] = {}

    return render(request, 'checkout.html', {'order': order})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after registration
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})