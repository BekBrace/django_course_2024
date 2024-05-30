from django.shortcuts import render, redirect

# Create your views here.
from .forms import ProductForm
from .models import Product

# CRUD = Create , Read, Update, Delete

# Home View
def home_view(request):
    return render(request, 'invApp/home.html')

# Create View
def product_create_view(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    return render(request, 'invApp/product_form.html', {'form':form})

# Read View
def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'invApp/product_list.html', {'products':products})

# Update View
def product_update_view(request, product_id):
    product = Product.objects.get(product_id=product_id)
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    return render(request, 'invApp/product_form.html', {'form':form})

# Delete View
def product_delete_view(request, product_id):
    product = Product.objects.get(product_id = product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'invApp/product_confirm_delete.html', {'product':product})
