from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.db.models import Q

from .models import Regular_Pizza, Sicilian_Pizza, Toppings, Sub

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": None})
    context = {
        "Regular_Pizza": Regular_Pizza.objects.all(),
        "Sicilian_Pizza": Sicilian_Pizza.objects.all(),
        "Toppings": Toppings.objects.all(),
        "Sub": Sub.objects.all()
    }
    return render(request, "orders/index.html", context)

def login_view(request):
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
        return redirect('index')
    else:
        return render(request, "orders/login.html", {"message": "Invalid credentials."})

def logout_view(request):
    logout(request)
    return redirect('index')

def order(request, name, option, size):
    new_order = {
        "username" : request.user.username,
        "name" : name,
        "option": option,
        "size" : size
    }
    
    if name == 'Regular Pizza':
        if size == 'small':
            new_order["price"] = Regular_Pizza.objects.get(topping=option).small
        else:
            new_order["price"] = Regular_Pizza.objects.get(topping=option).large
        if option != 'Cheese':
            if option == 'Special':
                new_order["options_num"] = 5
            else:
                new_order["options_num"] = int(option[0])
            new_order["extras"] = Toppings.objects.all()

    elif name == 'Sicilian Pizza':
        if size == 'small':
            new_order["price"] = Sicilian_Pizza.objects.get(item=option).small
        else:
            new_order["price"] = Sicilian_Pizza.objects.get(item=option).large
        if option != 'Cheese':
            if option == 'Special':
                new_order["options_num"] = 5
            else:
                new_order["options_num"] = int(option[0])
            new_order["extras"] = Toppings.objects.all()

    elif name == 'Sub':
        if size == 'small':
            new_order["price"] = Sub.objects.get(sub=option).small
        else:
            new_order["price"] = Sub.objects.get(sub=option).large

        if option == 'Steak + Cheese':
            new_order["extras"] = Sub.objects.filter(Q(sub__startswith='+') | Q(sub__startswith='Extra'))
        else:
            new_order["extras"] = Sub.objects.filter(sub__startswith='Extra')

    return render(request, "orders/order.html", new_order)