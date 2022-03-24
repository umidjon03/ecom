from django.db import models


# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=200)
    image = models.CharField(max_length=300)
    description = models.TextField()


class Orders(models.Model):
    items = models.CharField(max_length=303)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=303)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=80)
    zipcode = models.CharField(max_length=50)
