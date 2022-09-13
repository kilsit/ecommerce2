from django.shortcuts import render, redirect
from django.contrib import messages
from carts.models import  CartItem

# Create your views here.
def cart_dashboard(request):
    carts =  CartItem.objects.all()
    context = {
        'carts': carts
    }
    return render(request, "carts_dashboard/cart_dashboard.html", context)

def  cart_delete(request, pk):
    carts = CartItem.objects.get(id=pk)
    if request.method=='POST':
        carts.delete()
        messages.success(request, 'deleted successfully')
        return redirect('cart_dashboard')
    return render(request, "carts_dashboard/cart_delete.html")

