from django.contrib import admin
from .models import *

class OrderProductInline(admin.TabularInline):
    models = OrderProduct
    readonly_fields = ('payment', 'user', 'product', 'quantity')

class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'full_name', 'phone', 'email', 'city', 'ordered_total', 'tax', 'status', 'is_orderd', 'created_at']
    list_filter = ['status', 'is_ordered']
    search_fields = ['order_number', 'first_name', 'last_name', 'phone', 'email']
    list_per_page = 20
    inlines = [OrderProductInline]

admin.site.register(Payment)
admin.site.register(Order)
admin.site.register(OrderProduct)
