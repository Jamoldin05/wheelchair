

from django.contrib import admin
from .models import Category, Product, Order, Comment
# from import_export.admin import ImportExportActionModelAdmin




@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
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




@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['name','phone','quantity']
    list_filter = ['quantity']
    search_fields = ['name']




@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name','rating','email']
    list_filter = ['rating']
    search_fields = ['name']