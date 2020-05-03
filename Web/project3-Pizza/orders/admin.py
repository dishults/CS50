from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Regular_Pizza, Sicilian_Pizza, Topping, Sub, Pending, Placed

class Regular_Pizza_Admin(admin.ModelAdmin):
    list_display = ('topping', 'small', 'large')

class Sicilian_Pizza_Admin(admin.ModelAdmin):
    list_display = ('item', 'small', 'large')

class Sub_Admin(admin.ModelAdmin):
    list_display = ('sub', 'small', 'large')

class Order_Admin(admin.ModelAdmin):
    list_display = ('user', 'choice', 'option', 'size', 'price',
                    'extra1', 'extra2', 'extra3', 'extra4', 'extra5')

# Register your models here.
admin.site.register(Regular_Pizza, Regular_Pizza_Admin)
admin.site.register(Sicilian_Pizza, Sicilian_Pizza_Admin)
admin.site.register(Topping)
admin.site.register(Sub, Sub_Admin)
admin.site.register(Pending, Order_Admin)
admin.site.register(Placed, Order_Admin)