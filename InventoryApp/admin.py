from django.contrib import admin
from .models import Goods

@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display=('name','location','price')
    list_filter=('name','location')
    search_fields=('name','location','price')
