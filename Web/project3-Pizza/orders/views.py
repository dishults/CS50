from django.http import HttpResponse
from django.shortcuts import render

from .models import Regular_Pizza, Sicilian_Pizza, Toppings

# Create your views here.
def index(request):
    context = {
        "Regular_Pizza": Regular_Pizza.objects.all(),
        "Sicilian_Pizza": Sicilian_Pizza.objects.all(),
        "Toppings": Toppings.objects.all()
    }
    return render(request, "orders/index.html", context)
