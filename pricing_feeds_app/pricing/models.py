from django.db import models

class PricingRecord(models.Model):
    store_id = models.CharField(max_length=100)
    sku = models.CharField(max_length=100)
    product_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"{self.store_id} - {self.sku} - {self.product_name}"