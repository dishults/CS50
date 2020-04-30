from django.db import models

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

class Subs(models.Model):
    sub = models.CharField(max_length=50)
    small = models.FloatField()
    large = models.FloatField()

    def __str__(self):
        return f"{self.sub} {self.small} {self.large}"
