from django.contrib import admin
from .models import Category, Product, Order, User, Comment

from django.contrib import admin
from .models import Category, Product
from import_export.admin import ImportExportActionModelAdmin




@admin.register(Category)
class CategoryAdmin(ImportExportActionModelAdmin):
    list_display = ['id', 'title', 'count_products']

    def count_products(self,obj):
        return obj.products.count()
    
    count_products.short_description = 'All products'




@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [ 'name','price','category', 'is_stock']
    list_filter = ['category']
    search_fields = ['name']




    def is_stock(self,obj):
        return obj.stock > 0
    
    is_stock.boolen = True
