from django.contrib import admin
from shop.models import *

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(CustomUser)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'image']


admin.site.register(Offer)

class GalleryAdmin(admin.TabularInline):
    model = Gallery
    fk_name = 'product'
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [GalleryAdmin]

admin.site.register(Product, ProductAdmin)