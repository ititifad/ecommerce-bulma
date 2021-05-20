from django.contrib import admin

from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'date_added', 'updated']
    list_filter = ['date_added', 'updated']
    list_editable = ['price']
    prepopulated_fields = {'slug': ('name',)}
