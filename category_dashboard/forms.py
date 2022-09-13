from django import forms
from category.models import Category

class  CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name', 'slug']
        # fields = '__all__'