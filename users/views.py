from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import Userprofile
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from store.forms import ProductForm
from django.utils.text import slugify
from store.models import Product, Order, OrderItem

# Create your views here.
def vendor_detail(request, pk):
    user = User.objects.get(pk=pk)
    products = user.products.filter(status=Product.ACTIVE)
    return render(request, 'users/vendor_detail.html', {'products': products, 'user':user})

@login_required
def my_store(request):
    products = request.user.products.exclude(status=Product.DELETED)
    order_items = OrderItem.objects.filter(product__user=request.user).order_by('id')
    return render(request, 'users/my_store.html', {'products': products, 'order_items': order_items})

@login_required
def my_store_order_detail(request, pk):
    order = get_object_or_404(Order,pk=pk)

    return render(request, 'users/my_store_order_detail.html', {'order': order})

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            title = request.POST.get('title')
            product = form.save(commit=False)
            product.user = request.user
            product.slug = slugify(title)
            product.save()

            messages.success(request, 'The product was added')
            return redirect('my_store')
    else:
        form = ProductForm()
    return render(request, 'users/product_form.html', {'title': 'Add product', 'form': form})

@login_required
def edit_product(request, pk):
    product = Product.objects.filter(user=request.user).get(pk=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
                form.save()

                messages.success(request, 'The changes was saved!')
                return redirect('my_store')


    form = ProductForm(instance=product)
    return render(request, 'users/product_form.html', 
    {'title': 'Edit product',
     'product': product,
     'form': form})

@login_required
def delete_product(request, pk):
    product = Product.objects.filter(user=request.user).get(pk=pk)
    product.status = Product.DELETED
    product.save()

    messages.success(request, 'The product was deleted!')
    return redirect('my_store')

@login_required
def myaccount(request):
    return render(request, 'users/myaccount.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            user = Userprofile.objects.create(user=user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'users/signup.html', {'form': form})
