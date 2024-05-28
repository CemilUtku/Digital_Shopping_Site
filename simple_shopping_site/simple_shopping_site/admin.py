from django.contrib import admin
from .models import Product, Customer, Order, OrderItem

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image')

admin.site.register(Product, ProductAdmin)
admin.site.register(Customer)

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)