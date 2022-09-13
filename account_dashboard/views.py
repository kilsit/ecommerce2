from django.shortcuts import render, redirect
from accounts.models import Account
from django.contrib import messages
from .forms import  AccountForm
from django.views.generic import UpdateView
from django.urls import reverse_lazy, reverse
from django.contrib.messages.views import SuccessMessageMixin


def account(request):
    accounts = Account.objects.all() 
    context = {
        'accounts': accounts, 
    }
    return render(request, "admin_dashboard/account.html", context)

def account_delete(request, pk):
    accounts = Account.objects.get(id=pk)
    if request.method=='POST':
        accounts.delete()
        messages.success(request, 'deleted successfully')
        return redirect('account')
    return render(request, 'admin_dashboard/account_delete.html')

class UpdatePostView(UpdateView):
     model = Account
     form_class =  AccountForm
     template_name = 'admin_dashboard/account_update.html'
     def get_success_url(self):
        return reverse('Success')
     success_message = 'updated successfully'
     success_url = reverse_lazy('account')

# def account_update(request, pk):
#       accounts = Account.objects.get(id=pk)
#       if request.method == 'POST':
#           form = AccountForm(request.POST, request.FILES, instance=accounts)
#           if form.is_valid():
#               form.save()
#               messages.success(request, 'updated successfully')
#               return redirect('account')
#       else:
#           form = AccountForm(instance=accounts)
#       context ={
#           'form': form,
#       }
#       return render(request, "admin_dashboard/account_update.html", context)