from django.contrib import admin
from .models import Organisation,Branch,Customer,Order,Product

admin.site.register(Organisation)
admin.site.register(Branch)
admin.site.register(Customer)
admin.site.register(Product)

@admin.register(Order) 
class OrderAdmin(admin.ModelAdmin):
    list_display = ('cust_name', 'product_name', 'comments')

