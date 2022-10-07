from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','price','stock','category','created_date','is_available')
    prepopulated_fields = {'slug':('product_name',)}
admin.site.register(Product,ProductAdmin)

class VariationAdmin(admin.ModelAdmin):
    list_display = ('product','variation_category','variation_value','is_active')
    list_editable = ('is_active',)
    list_filter = ('product','variation_category','variation_value',)
admin.site.register(Variation,VariationAdmin)



class ReviewRatingAdmin(admin.ModelAdmin):
    list_display = ('product','user','review','rating','created_at')
admin.site.register(ReviewRating,ReviewRatingAdmin)