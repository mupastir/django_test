from django.contrib import admin
from .models import Goods, Category, Order


class GdsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'date', 'category')
    list_display_links = ('name',)
    search_fields = ('name', 'brand', 'color')


admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Goods, GdsAdmin)
