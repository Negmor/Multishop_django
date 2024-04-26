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


class Category(models.Model):
    parent = models.ForeignKey("self", blank=True, null=True, on_delete=models.CASCADE, related_name="subs")
    title = models.CharField(max_length=100)
    slug = models.SlugField()

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ManyToManyField(Category,blank=True,null=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    price = models.IntegerField()
    discount = models.SmallIntegerField()
    image = models.ImageField(upload_to="products")
    size = models.ManyToManyField(Size, blank=True, null=True, related_name="products")
    color = models.ManyToManyField(Color, related_name="products")

    def __str__(self):
        return self.title


class Information(models.Model):
    text = models.TextField()
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE, related_name="informations")

    def __str__(self):
        return self.text[:30]
