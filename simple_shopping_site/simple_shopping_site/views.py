from django.shortcuts import render, redirect
from .models import Product, Customer 
from .forms import CustomerForm, ProductForm

def home(request):
    customers = Customer.objects.all()  # Müşterileri al
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
