from django.contrib import admin
from .models import * 
import admin_thumbnails

@admin_thumbnails.thumbnail('images')
class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category', 'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}
    inlines = [ProductGalleryInline]

class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category', 'variation_value', 'is_active')
    list_editable = ['is_active']
    list_filter = ('product', 'variation_category', 'variation_value')
# class PropertiesAdmin(admin.ModelAdmin):
#     list_display = ('color', 'size')

admin.site.register(ProductGallery) 
admin.site.register(Product, ProductAdmin)
# admin.site.register(Properties, PropertiesAdmin)
admin.site.register(Variation, VariationAdmin)
admin.site.register(ReviewRating)


 
