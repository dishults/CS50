from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.db.models import Q

from .models import Regular_Pizza, Sicilian_Pizza, Topping, Sub, Pending, Placed

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": None})
    context = {
        "Regular_Pizza": Regular_Pizza.objects.all(),
        "Sicilian_Pizza": Sicilian_Pizza.objects.all(),
        "Topping": Topping.objects.all(),
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
            new_order["extras"] = Topping.objects.all()

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
            new_order["extras"] = Topping.objects.all()

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

def shoppint_cart(request):
    username = request.user.username
    o = Pending.objects.create(user=User.objects.get(username=username),
                            choice=request.POST["name"],
                            option=request.POST["option"],
                            size=request.POST["size"],
                            price=float(request.POST["price"]))
    if "extras" in request.POST:
        extras = request.POST.getlist("extras")
        o.extra1 = extras[0]
        if len(extras) > 1:
            o.extra2 = extras[1]
            if len(extras) > 2:
                o.extra3 = extras[2]
                if len(extras) > 3:
                    o.extra4 = extras[3]
                    if len(extras) > 4:
                        o.extra5 = extras[4]
        if o.choice == 'Sub':
            o.price += 0.5 * len(extras)
        o.save()

    return redirect('index')

def delete(request, order_nb):
    Pending.objects.get(pk=order_nb).delete()

    return redirect('checkout')

def checkout(request):
    username = request.user.username
    orders = Pending.objects.filter(user=username)
    
    return render(request, "orders/checkout.html", { "orders" : orders })

def placed(request):
    username = request.user.username
    pending = Pending.objects.filter(user=username)
    for p in pending:
        Placed.objects.create(user=p.user,
                                choice=p.choice,
                                option=p.option,
                                size=p.size,
                                price=p.price,
                                extra1=p.extra1,
                                extra2=p.extra2,
                                extra3=p.extra3,
                                extra4=p.extra4,
                                extra5=p.extra5)
    pending.delete()

    return redirect('index')

def status(request):
    username = request.user.username
    orders = Placed.objects.filter(user=username)
    
    return render(request, "orders/status.html", { "orders" : orders })