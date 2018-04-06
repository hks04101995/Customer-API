from django.db import models

class ProductProduct(models.Model):
    product_name = models.CharField('Product', max_length=40)
    reference = models.CharField('SKU', max_length=40)
    product_type = models.CharField(choices=(('product',"Stockable"),('consu',"Consumable"),('service',"Service")),name='Type', default='product',max_length=50)
    quantity = models.IntegerField('Quantity')
    price = models.FloatField('Price', default='1.0')
    USERNAME_FIELD = 'product_name'
    REQUIRED_FIELDS = ['product_name','product_type']

    def __str__(self):
        return self.product_name
