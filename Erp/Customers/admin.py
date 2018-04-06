from django.contrib import admin
from .models import ResPartner
from .product import ProductProduct
from .saleorder import *
# Register your models here.


admin.site.register(ResPartner)
admin.site.register(ProductProduct)
admin.site.register(SaleOrder)
admin.site.register(SaleOrderLine)
