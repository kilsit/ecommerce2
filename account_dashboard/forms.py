from django import forms
from accounts.models import Account

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = '__all__'
        # fields = ['email', 'first_name', 'last_name', 'username', 'phone_number', 'is_admin', 'is_staff', 'is_superadmin', 'is_active']

    # def __init__(self, *args, **kwargs):
    #     super(AccountForm, self).__init__(*args, **kwargs)
    #     for field in self.fields:
    #         self.fields[field].widget.attrs['class'] = 'form-control'





# class ProductFullForm(ProductForm):
#     productGallery = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
#     class Meta(ProductForm.Meta):
#         fields = ProductForm.Meta.fields + ['productGallery',]