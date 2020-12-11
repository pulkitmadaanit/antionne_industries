from django.contrib import admin
from .models import HomeSlider , ClientSlider , Product

# Register your models here.
# admin.site.register(Product)
# admin.site.register(HomeSlider)
# admin.site.register(ClientSlider)
@admin.register(HomeSlider)
class HomeSliderAdmin(admin.ModelAdmin):
    list_display = ('id', 'images', 'description')

@admin.register(ClientSlider)
class ClientSliderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'images', 'description')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'images', 'description')