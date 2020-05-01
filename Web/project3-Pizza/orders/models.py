from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Regular_Pizza(models.Model):
    topping = models.CharField(max_length=11)
    small = models.FloatField()
    large = models.FloatField()

    def __str__(self):
        return f"{self.topping} {self.small} {self.large}"

class Sicilian_Pizza(models.Model):
    item = models.CharField(max_length=11)
    small = models.FloatField()
    large = models.FloatField()

    def __str__(self):
        return f"{self.item} {self.small} {self.large}"

class Toppings(models.Model):
    topping = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.topping}"

class Sub(models.Model):
    sub = models.CharField(max_length=50)
    small = models.FloatField()
    large = models.FloatField()

    def __str__(self):
        return f"{self.sub} {self.small} {self.large}"

# Shopping cart models

#class Pizza_Order(models.Model):
#    username = models.ForeignKey(User, on_delete=models.CASCADE)
#    pizza = models.CharField(max_length=15)
#    size = models.CharField(max_length=5)
#    topping1 = models.ForeignKey(Toppings, on_delete=models.CASCADE, related_name="topping1")
#    topping2 = models.ForeignKey(Toppings, on_delete=models.CASCADE, related_name="topping2")
#    topping3 = models.ForeignKey(Toppings, on_delete=models.CASCADE, related_name="topping3")
#    topping4 = models.ForeignKey(Toppings, on_delete=models.CASCADE, related_name="topping4")
#    topping5 = models.ForeignKey(Toppings, on_delete=models.CASCADE, related_name="topping5")
#
#    users = models.ManyToManyField(User, blank=True, related_name="pizzas")
#
#class Sub_Order(models.Model):
#    username = models.ForeignKey(User, on_delete=models.CASCADE)
#    sub = models.CharField(max_length=15)
#    extra1 = models.ForeignKey(Toppings, on_delete=models.CASCADE, related_name="extra1")
#    extra2 = models.ForeignKey(Toppings, on_delete=models.CASCADE, related_name="extra2")
#    extra3 = models.ForeignKey(Toppings, on_delete=models.CASCADE, related_name="extra3")
#    extra4 = models.ForeignKey(Toppings, on_delete=models.CASCADE, related_name="extra4")
#    extra5 = models.ForeignKey(Toppings, on_delete=models.CASCADE, related_name="extra5")
#
#    users = models.ManyToManyField(User, blank=True, related_name="subs")