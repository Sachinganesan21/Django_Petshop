from django.contrib import admin
from .models import Product,Category

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=('id','Product_name','Product_description','Product_price','Product_brand','category')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('id','category_name','slug')

#admin.site.register(Product,ProductAdmin)

