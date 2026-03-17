from django.db import models
from django.utils import timezone

# Create your models here.

class Supplier(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now)

    def getName(self):
        return self.name
    
    def __str__(self):
        return "{} - {}, {} created at: {}".format(self.name, self.city, self.country, self.created_at)
    
class WaterBottle(models.Model):

    sku = models.CharField(max_length=200, unique = True)
    brand = models.CharField(max_length=200)
    cost = models.DecimalField(max_digits=10, decimal_places = 2)
    size = models.CharField(max_length=200)
    mouthSize = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    suppliedBy = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    qty = models.IntegerField(default = 0)
    # https://www.geeksforgeeks.org/python/django-model-data-types-and-fields-list/

    def __str__(self): 
        return "{}: {}, {}, {}, {}, supplied by {}, {} : {}".format(self.sku,self.brand, self.mouthSize, self.size, self.color, self.suppliedBy, self.cost, self.qty)
