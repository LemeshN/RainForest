from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from .forms import ProductForm, OrderForm
from .models import Product, Order


def home(request):
    products = Product.objects.all()
    context = {'title': 'Home page', 'products': products}
    return render(request, 'home.html', context)


def add_product(request):
    error = ''
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Form is not valid'

    form = ProductForm()
    context = {'form': form,
               'error': error}
    return render(request, 'add_product.html', context)


def product_detail(request, id):
    products = Product.objects.filter(id=id)
    context = {'products': products}
    return render(request, 'product_detail.html', context)


def product_delete(request, id):
    try:
        product = Product.objects.get(id=id)
        product.delete()
        return redirect('home')
    except Product.DoesNotExist:
        return HttpResponseNotFound('Product not found')


def update(request, id):
    try:
        product = Product.objects.get(id=id)

        if request.method == 'POST':
            product.cost = request.POST.get('cost')
            product.price = request.POST.get('price')
            product.quantity = request.POST.get('quantity')
            product.save()
            return redirect('home')
        else:
            return render(request, 'update.html', {'product': product})
    except Product.DoesNotExist:
        return HttpResponseNotFound('Product not found')


def add_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form = Order(
                quantity=form.cleaned_data['quantity']
            )
            form.save()
            return redirect('home')
        else:
            error = 'Form is not valid'

    form = OrderForm()
    context = {'form': form}
    return render(request, 'add_order.html', context)
