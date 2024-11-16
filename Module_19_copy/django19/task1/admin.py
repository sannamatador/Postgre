from django.contrib import admin
from .models import Goods


@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

# Register your models here.
