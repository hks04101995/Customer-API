from django.db import models
from .models import ResPartner
from . import product
import logging
logger = logging.getLogger(__name__)
class SaleOrder(models.Model):
    customer = models.ForeignKey(ResPartner,verbose_name ='Customer')
    ordernumber = models.CharField('Name',max_length=50,)
    total = models.FloatField(verbose_name = 'Total', blank=True)
    def __str__(self):
        return self.ordernumber

class SaleOrderLine(models.Model):
    # line_id = models.AutoField("Order Line Id")
    saleorder = models.ForeignKey(SaleOrder,verbose_name  = 'Sale Order')
    product = models.ForeignKey(product.ProductProduct, verbose_name ='Product')
    product_price = models.FloatField('Price', default= 1.0)
    qty = models.IntegerField('Quantity', default= 1)

    def __str__(self):
        return self.product.product_name

    def save(self, *arg, **args):
        if not self.product_price:
            self.product_price = product.price
        self.product_price = self.product_price*self.qty
        rec = super(SaleOrderLine,self).save(*arg, **args)
        total = 0.0
        order = SaleOrder.objects.get(ordernumber=self.saleorder)
        lines =SaleOrderLine.objects.filter(saleorder=self.saleorder.id)
        for line in lines:
            total += line.product_price
        total += self.product_price
        order.total = total
        order.save()
        return rec
