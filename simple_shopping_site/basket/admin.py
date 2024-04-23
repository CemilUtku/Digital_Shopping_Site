from django.contrib import admin
from simple_shopping_site.models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image')

admin.site.register(Product, ProductAdmin)
admin.site.register(Customer)