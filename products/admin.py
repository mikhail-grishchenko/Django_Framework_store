from django.contrib import admin
from products.models import ProductCategory, ProductSubcategory, Product, Basket

admin.site.register (ProductCategory)
admin.site.register (ProductSubcategory)
admin.site.register (Basket)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category', 'subcategory')
    fields = ('name', 'image', 'description', 'short_description', 'price', 'quantity', 'category', 'subcategory')
    search_fields = ('name', 'description', 'short_description', 'price', 'quantity',)


class BasketAdminInLine(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp',)
    readonly_fields = ('product', 'created_timestamp',)
    extra = 0
