from django.db import models
from django.urls import reverse

class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=100, decimal_places=2)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product-detail", kwargs={"pk" : self.pk})
        
        