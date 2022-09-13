from unicodedata import category
from django.shortcuts import redirect, render
from django.template import context
from accounts.models import Account
from orders.models import Order
from store.models import Product,  ProductGallery
from django.contrib import messages, auth
from store.models import Variation
from .forms import *



# Create your views here.

def admin_dashboard(request):
    # if not request.user.is_staff:
    #         return redirect('login')
    accounts = Account.objects.all()
    order = Order.objects.all()
    product = Product.objects.all()
    a=0
    o=0
    p=0
    for i in accounts:
        a+=1
    for i in order:
        o+=1
    for i in product:
        p+=1
    context ={
        'a': a,
        'o': o,
        'p': p,
    }
    return render(request, 'admin_dashboard/home_admin.html', context)

def variation(request):
    variations = Variation.objects.all()
    if request.method == 'POST':
          form = VariationForm(request.POST,request.FILES)
          if form.is_valid():
            form.save()
            messages.success(request, 'added successfully')
            return redirect('variation')
    else:
        form = VariationForm()
    context ={
        'variations': variations,
        'form': form
    }
    return render(request, "store_dashboard/variation.html", context)



def variation_delete(request, pk):
    variations = Variation.objects.get(id=pk)
    if request.method=='POST':
        variations.delete()
        messages.success(request, 'deleted successfully')
        return redirect('variation')
    return render(request, 'store_dashboard/variation_delete.html')

def variation_update(request, pk):
      variations = Variation.objects.get(id=pk)
      if request.method == 'POST':
          form = VariationForm(request.POST, request.FILES, instance=variations)
          if form.is_valid():
              form.save()
              messages.success(request, 'updated successfully')
              return redirect('variation')
      else:
          form = VariationForm(instance=variations)
      context ={
          'form': form,
      }
      
      return render(request, "store_dashboard/variation_update.html", context)


def store_dashboard(request):
    products = Product.objects.all().filter(is_available=True).order_by('id')   
    context = {
        'products': products, 
    }

    return render(request, "store_dashboard/store.html", context)

def store_dashboard_delete(request, product_slug):
    products = Product.objects.get(slug=product_slug)
    if request.method=='POST':
        products.delete()
        messages.success(request, 'deleted successfully')
        return redirect('store_dashboard')
    return render(request, 'store_dashboard/store_delete.html')

def store_form(request):
    #   products = Product.objects.all()
      products = Product.objects.all().filter(is_available=True).order_by('id')  
      if request.method == 'POST':
          form = ProductForm(request.POST,request.FILES)
          if form.is_valid():
            form.save()
            messages.success(request, 'added successfully')
            return redirect('store_dashboard')
      else:
          form = ProductForm()
      context ={
          'form': form,
          'products': products
      }
      
      return render(request, "store_dashboard/store_form.html", context)

def store_dashboard_update(request, product_slug):
      products = Product.objects.get(slug=product_slug)
      if request.method == 'POST':
          form = ProductForm(request.POST, request.FILES, instance=products)
          if form.is_valid():
              form.save()
              messages.success(request, 'updated successfully')
              return redirect('store_dashboard')
      else:
          form = ProductForm(instance=products)
      context ={
          'form': form,
      }
      
      return render(request, "store_dashboard/store_update.html", context)

def  productgallery(request):
    #   products = Product.objects.all()
      gallery = ProductGallery.objects.all()  
      if request.method == 'POST':
          form =  ProductGalleryForm(request.POST,request.FILES)
          if form.is_valid():
            form.save()
            messages.success(request, 'added successfully')
            return redirect('store_dashboard')
      else:
          form = ProductGalleryForm()
      context ={
          'form': form,
          'gallery': gallery
      }
      
      return render(request, "store_dashboard/gallery.html", context)


# def store_dashboard(request):
#         products = Product.objects.all().filter(is_available=True).order_by('id')
#         if request.method == "POST":
#            form = ProductFullForm(request.POST or None, request.FILES or None)
#            if form.is_valid():
#                 form.save()
#                 return redirect('store_dashboard')
#         else:
#             form = ProductFullForm()
#         context ={
#             'form': form,
#             'products': products,
#         }
            
#         return render(request, "store_dashboard/store_form.html", context)


