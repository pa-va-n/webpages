from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, MenuItemForm, RegisterForm
from .models import MenuItem
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.views.decorators.http import require_POST
from django.http import Http404

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  
            user.save()
            return redirect('login')  
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.info(request, f"Hello, {user.username}!")
            return redirect('view_menus')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, "LOGGED OUT ")
    return redirect('login')

@login_required
def menu_list(request):
    items = MenuItem.objects.all()
    return render(request, 'view_menus.html', {'menus': items})

@login_required
def add_menu_item(request):
    if not request.user.is_admin:
        return redirect('view_menus')
    if request.method == 'POST':
        form = MenuItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_menus')
    else:
        form = MenuItemForm()
    return render(request, 'add_menu.html', {'form': form})

@login_required
def cart_view(request):
    cart = request.session.get('cart', [])
    return render(request, 'cart.html', {'cart': cart})

@login_required
def add_to_cart(request, item_id):
    if 'cart' not in request.session:
        request.session['cart'] = []

    try:
        item = MenuItem.objects.get(id=item_id)
    except MenuItem.DoesNotExist:
        raise Http404("No MenuItem matches the given query.")

    cart_item = {
        'id': item.id,  
        'title': item.title,
        'price': str(item.price)  
    }
    request.session['cart'].append(cart_item)
    request.session.modified = True  
    return redirect('view_menus')

from django.contrib import messages

@login_required
@require_POST
def remove_from_cart(request, item_id):
    cart = request.session.get('cart', [])
    new_cart = [item for item in cart if item['id'] != item_id]
    if len(cart) > len(new_cart):
        messages.success(request, "Item removed successfully.")
    request.session['cart'] = new_cart
    request.session.modified = True
    return redirect('cart')

login_required
def checkout_view(request):
    if request.method == 'POST':
        request.session.pop('cart', None)  
        return redirect('checkout_complete')  
    else:
        return render(request, 'checkout.html', {'cart': request.session.get('cart', [])})
    
@login_required
def checkout_complete_view(request):
    return render(request, 'checkout_complete.html')