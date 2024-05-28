from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Customer, Order, OrderItem
from .forms import CustomerForm, ProductForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User

def home(request):
    customers = Customer.objects.all()
    return render(request, 'home.html', {'customers': customers})

def list_customers(request):
    customers = Customer.objects.all()
    return render(request, 'list_customers.html', {'customers': customers})

def create_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CustomerForm()
    return render(request, 'create_customer.html', {'form': form})

def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = ProductForm()
    return render(request, 'create_product.html', {'form': form})

def process_order(request):
    if request.method == 'POST':
        # Alışveriş sepetindeki ürünleri al
        basket_items = Order.objects.filter(user=request.user)

        # Stok kontrolü yap
        out_of_stock = []
        for item in basket_items:
            if item.quantity > item.product.stock:
                out_of_stock.append(item.product.name)

        if out_of_stock:
            # Stokta olmayan ürünler varsa işlemi iptal et
            return render(request, 'order_failed.html', {'out_of_stock': out_of_stock})

        # Stokta yeterli miktarda ürün varsa siparişi işle
        customer = Customer.objects.get(user=request.user)
        order = Order.objects.create(customer=customer)
        for item in basket_items:
            OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity)
            item.product.stock -= item.quantity
            item.product.save()

        # Sepeti temizle
        basket_items.delete()
        return redirect('order_success')

    return render(request, 'process_order.html')

def list_orders(request):
    if request.user.is_authenticated:
        customer = request.user.customer if hasattr(request.user, 'customer') else None
        if not customer:
            customer = Customer.objects.create(user=request.user)
        orders = Order.objects.filter(user=customer)
        return render(request, 'list_orders.html', {'orders': orders})
    else:
        return render(request, 'error.html', {'message': 'You are not authorized to view this page.'})
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully registered!')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/sign_up.html', {'form': form})