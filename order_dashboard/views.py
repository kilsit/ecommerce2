from django.shortcuts import render, redirect
from orders.models import Order, OrderProduct
from .forms import OrderForm
from django.contrib import messages
# Create your views here.
def order_dashboard(request):
    orders = Order.objects.all() 
    if request.method == 'POST':
        form = OrderForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = OrderForm()      
    context = {
        'orders': orders,
         'form': form,
    }
    return render(request, "admin_dashboard/order.html", context)

def  order_dashboard_delete(request, pk):
    products = Order.objects.get(id=pk)
    if request.method=='POST':
        products.delete()
        messages.success(request, 'deleted successfully')
        return redirect('order_dashboard')
    return render(request, 'admin_dashboard/order_delete.html')

def order_product(request):
    order_products = OrderProduct.objects.all()
    context = {
        'order-products': order_products
    }
    return render(request, "admin_dashboard/order_product.html", context)