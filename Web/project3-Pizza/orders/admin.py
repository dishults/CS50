from django.contrib import admin

from .models import Regular_Pizza, Sicilian_Pizza, Toppings

# Register your models here.
admin.site.register(Regular_Pizza)
admin.site.register(Sicilian_Pizza)
admin.site.register(Toppings)