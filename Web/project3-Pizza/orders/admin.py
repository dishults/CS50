from django.contrib import admin

from .models import Regular_Pizza, Sicilian_Pizza, Toppings, Subs

class Regular_Pizza_Admin(admin.ModelAdmin):
    list_display = ('topping', 'small', 'large')

class Sicilian_Pizza_Admin(admin.ModelAdmin):
    list_display = ('item', 'small', 'large')

class Subs_Admin(admin.ModelAdmin):
    empty_value_display = 'unknown'
    list_display = ('sub', 'small', 'large')

# Register your models here.
admin.site.register(Regular_Pizza, Regular_Pizza_Admin)
admin.site.register(Sicilian_Pizza, Sicilian_Pizza_Admin)
admin.site.register(Toppings)
admin.site.register(Subs, Subs_Admin)