from dataclasses import fields
from django import forms
from store.models import Product,  Variation,  ProductGallery

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'slug', 'description', 'price', 'image', 'stock', 'category']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

class VariationForm(forms.ModelForm):
    class Meta:
        model =  Variation
        fields = ['product', 'variation_category', 'variation_value', 'is_active']

class ProductGalleryForm(forms.ModelForm):
    class Meta:
        model = ProductGallery
        fields = ['product', 'images']

    def __init__(self, *args, **kwargs):
        super( ProductGalleryForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

# class ProductFullForm(ProductForm):
#     productGallery = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
#     class Meta(ProductForm.Meta):
#         fields = ProductForm.Meta.fields + ['productGallery',]

# class NoteForm(forms.ModelForm):
#     class Meta:
#         model = Note
#         fields = ['title','text'] #make sure to mention field here, if nothing is mentioned then all will be required.

# class NoteFullForm(NoteForm): #extending form
#     images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

#     class Meta(NoteForm.Meta):
#         fields = NoteForm.Meta.fields + ['images',]