from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Regular_Pizza, Sicilian_Pizza, Toppings, Subs

# Create your views here.
def index(request):
    context = {
        "Regular_Pizza": Regular_Pizza.objects.all(),
        "Sicilian_Pizza": Sicilian_Pizza.objects.all(),
        "Toppings": Toppings.objects.all(),
        "Subs": Subs.objects.all()
    }
    return render(request, "orders/index.html", context)

def login_view(request):
    if request.method == 'GET':
        return render(request, "orders/login.html", {"message": None})
    username = request.POST["username"]
    password = request.POST["password"]

    if "register" in request.POST:
        email = request.POST["email"]
        user = User.objects.create_user(username, email, password)
        user.first_name = request.POST["first name"]
        user.last_name = request.POST["last name"]
        user.save()

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, "orders/login.html", {"message": "You're logged in."})
    else:
        return render(request, "orders/login.html", {"message": "Invalid credentials."})

def logout_view(request):
    logout(request)
    return render(request, "orders/login.html", {"message": "Logged out."})