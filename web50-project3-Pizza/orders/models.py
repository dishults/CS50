from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

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

class Topping(models.Model):
    topping = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.topping}"

class Sub(models.Model):
    sub = models.CharField(max_length=50)
    small = models.FloatField()
    large = models.FloatField()

    def __str__(self):
        return f"{self.sub} {self.small} {self.large}"

class Order(models.Model):
    user = models.ForeignKey(User, to_field="username", on_delete=models.CASCADE)

    choice = models.CharField(max_length=50)
    option = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    price = models.FloatField()
    extra1 = models.CharField(max_length=50, blank=True)
    extra2 = models.CharField(max_length=50, blank=True)
    extra3 = models.CharField(max_length=50, blank=True)
    extra4 = models.CharField(max_length=50, blank=True)
    extra5 = models.CharField(max_length=50, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return (f"{self.user} - {self.choice} - {self.option} "
                f"- {self.size} - {self.price}$\n"
                f"{self.extra1} - {self.extra2} - {self.extra3} "
                f"- {self.extra4} - {self.extra5}")

STATUS_CHOICES = [
    ('r', mark_safe("<span style='color:red;'>Recieved</span>")),
    ('p', mark_safe("<span style='color:orange;'>Prepaired</span>")),
    ('w', mark_safe("<span style='color:green;'>Withdrawn</span>")),
]

class Pending(Order):
    pass

class Placed(Order):
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
