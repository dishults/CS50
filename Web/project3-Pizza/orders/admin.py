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

class Pending_Admin(admin.ModelAdmin):
    list_display = ('user', 'choice', 'option', 'size', 'price',
                    'extra1', 'extra2', 'extra3', 'extra4', 'extra5')
    list_filter = ('user', 'choice')

def make_recieved(modeladmin, request, queryset):
    queryset.update(status='r')
make_recieved.short_description = "Mark as recieved"

def make_prepaired(modeladmin, request, queryset):
    queryset.update(status='p')
make_prepaired.short_description = "Mark as prepaired"

def make_withdrawn(modeladmin, request, queryset):
    queryset.update(status='w')
make_withdrawn.short_description = "Mark as withdrawn"

class Placed_Admin(admin.ModelAdmin):
    list_display = ('user', 'choice', 'option', 'size', 'price',
                    'extra1', 'extra2', 'extra3', 'extra4', 'extra5', 'status')
    list_filter = ('user', 'choice', 'status')
    actions = [make_recieved, make_prepaired, make_withdrawn]

# Register your models here.
admin.site.register(Regular_Pizza, Regular_Pizza_Admin)
admin.site.register(Sicilian_Pizza, Sicilian_Pizza_Admin)
admin.site.register(Topping)
admin.site.register(Sub, Sub_Admin)
admin.site.register(Pending, Pending_Admin)
admin.site.register(Placed, Placed_Admin)