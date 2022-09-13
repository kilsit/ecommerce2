from django.shortcuts import render
from category.models import Category
from django.shortcuts import render, redirect
from .forms import CategoryForm
from django.contrib import messages


def  add_category(request):
    if request.method == 'POST':
          form = CategoryForm(request.POST, request.FILES)
          if form.is_valid():
            form.save()
            messages.success(request, 'added successfully')
            return redirect('category')
    else:
        form = CategoryForm()
    context ={
        'form': form,
    }
    return render(request, "category_dashboard/add_category.html", context)



def category(request):
    return render(request, "category_dashboard/category.html")

def category_delete(request, pk):
        category = Category.objects.get(id=pk)
        category.delete()
        messages.success(request, 'deleted successfully')
        return redirect('category')

def category_update(request, pk):
    category = Category.objects.get(id=pk) 
    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'updated successfully')
            return redirect('category')
    else:
        form = CategoryForm(instance=category) 
    context = {
        'form': form,
    }
    return render(request, "category_dashboard/category_update.html", context)





