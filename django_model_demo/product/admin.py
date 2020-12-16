from django.contrib import admin

from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'description','price']
    ordering = ['title']
  # actions = [make_published]

# Register your models here.
admin.site.register(Product,ProductAdmin)
