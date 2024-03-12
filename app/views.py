from django.shortcuts import render,redirect
from app.models import Producttable,Signuptable,Signintable,Productaccessoriestable,Carttable,Billtable
import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.core.exceptions import MultipleObjectsReturned
from django.http import HttpResponseRedirect

# Create your views here.

def home(request):
    return render(request, 'index.html')

def sign_in(request):
    return render(request, 'signin.html')

def sign_up(request):
    return render(request, 'signup.html')

def success(request):
    return render(request, 'success.html')

def sign_error(request):
    return render(request, 'test.html')

def deliverto(request):
    return render(request, 'deliver.html')

def paymentmethod(request):
    return render(request, 'payment.html')

def order(request):
    return render(request, 'ordersuccess.html')

@login_required(login_url='sign_error') 
def addedmsg(request):
    return render(request, 'added2cart.html')

def lout(request):
    logout(request)
    return redirect ("home")



@login_required(login_url='sign_error') 
def show_cart(request):
    return render(request, 'cart.html')



def sign_up_form(request):
    if request.method == "POST":
        a = request.POST["fname"]
        b = request.POST["lname"]
        c = request.POST["mob"]
        d = request.POST["email"]
        g = request.POST["address"]
        h = request.POST["pincode"]
        e = request.POST["username"]
        f = request.POST["password"]

        try:
       
            exist_user = Signintable.objects.get(Username=e)
            return render(request, 'error.html', {'error_message': 'Username already exists'})
        except:
            l = Signintable(Username=e, Password=f)
            l.save()
            m = Signuptable(Firstname=a, Lastname=b, Mobile=c, Email=d, Address=g,Pincode=h, Username=e, Password=f)
            m.save()
            return render(request, 'success.html')

    return render(request, 'signup.html')



def login_form(request):
    try:
        if request.method == "POST":
            a = request.POST["user"]
            b = request.POST["pass"]


            users_with_username = Signintable.objects.filter(Username=a)

            if not users_with_username.exists():
                return render(request, "error.html", {'error_message': 'User not found'})

            if users_with_username.count() > 1:
   
                return render(request, "error.html", {'error_message': 'Multiple users with the same username'})

            q = users_with_username.first()

            if q.Password == b:
                request.session["member_id"] = q.id
                return redirect ("home")
            else:
                return render(request, "error.html", {'error_message': 'Incorrect password'})
    except MultipleObjectsReturned:
   
        return render(request, "error.html", {'error_message': 'Error: Multiple objects returned for the same username'})



def show_cameras(request):
    a = Producttable.objects.all()
    return render(request, 'cameras.html',{ 'products': a })


def show_product(request,id1):
    a = Producttable.objects.get(pk=id1)
    return render(request, 'all_product_view.html',{ 'products': a }) 

def show_accessories(request):
    a = Productaccessoriestable.objects.all()
    return render(request, 'accessories.html',{ 'products': a })

@login_required(login_url='sign_error') 
def to_cart(request, id2):
    b = Producttable.objects.get(pk=id2)
    return render(request, 'cart.html',{ 'products': b }) 

def usercart(request, id4, id5, id):
    Pid = id4
    Pname = id5
    Price = id

    if request.method == "POST":
        c = request.POST["name3"]
        total = int(c) * int(Price)
        q = Carttable(Productid=Pid, Productname=Pname, Quantity=c, price=total, Userid=request.session["member_id"])
        q.save()
        a = Billtable(Productid=Pid, Productname=Pname, Quantity=c, price=total, Userid=request.session["member_id"],
                      Date=datetime.date.today())
        a.save()
        # Render the success template instead of redirecting
        return render(request, "added2cart.html")

    return render(request, "cart1.html")






