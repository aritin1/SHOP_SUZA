from django.contrib import admin

from .models import *

# admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Product)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')
    # ordering = ("id",)
