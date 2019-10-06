from django.contrib import admin
from marketplace.models import Product, Client
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    pass


class ClientAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)
admin.site.register(Client, ClientAdmin)
