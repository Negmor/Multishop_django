from django.db import models

# Create your models here.
from account.models import User
from product.models import Product


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    created_at = models.DateTimeField(auto_now_add=True)
    total = models.IntegerField(default=0)
    is_paid = models.BooleanField(default=False)
    address=models.TextField(default="")

    def __str__(self):
        return self.user.phone


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="items")
    size = models.CharField(max_length=12)
    color = models.CharField(max_length=12)
    quantity = models.SmallIntegerField(default=1)
    price = models.PositiveIntegerField()


class DiscountModel(models.Model):
    name = models.CharField(max_length=10,unique=True)
    percent = models.SmallIntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.name
