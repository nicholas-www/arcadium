from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, default="Undefined")

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    quantity = models.IntegerField(null=False, blank=False, default=0)
    description = models.TextField(null=False, blank=False)

    def __str__(self):
        return f'{self.name} - [{self.category}]'
