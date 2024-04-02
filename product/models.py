from django.db import models


# Create your models here.

class Size(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Color(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    price = models.IntegerField()
    discount = models.SmallIntegerField()
    image = models.ImageField(upload_to="products")
    size = models.ManyToManyField(Size, blank=True,null=True,related_name="products")
    color = models.ManyToManyField(Color, related_name="products")




    def __str__(self):
        return self.title
