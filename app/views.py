from django.shortcuts import render,redirect
from app.models import Report 
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
def signup(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        if User.objects.filter(username=username).exists():
            return render(request,"signup.html",{"error":"Username already exist"})
        user=User.objects.create_user(username=username,password=password)
        user.save()
        login(request,user)
        return redirect("home")
    return render(request,"signup.html")
def forget(request):
    return render(request,"forget.html")
def loginuser(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("/home")
        else:
            return render(request,"login.html",{"error":"username or password invalid"})

    return render(request,"login.html")
@login_required
def home(request):
    return render(request,"index.html") 
def report(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        select=request.POST.get("select")
        message=request.POST.get("message")
        source=request.POST.get("source")
        date2=request.POST.get("date")
        Report.objects.create(name=name,email=email,select=select,message=message,source=source, date2=date2 or None)
        messages.success(request,"Your form is submit")
    return render(request,"report.html")
def scam(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        select=request.POST.get("select")
        platform=request.POST.get("platform")
        date2=request.POST.get("date")
        amount=request.POST.get("amount")
        message=request.POST.get("message")
        source=request.POST.get("source")
        Report.objects.create(name=name,email=email,select=select,platform=platform,date2=date2,message=message,source=source,amount=amount)
        messages.success(request,"Your form is submit")
    return render(request,"scam.html")
def somethingelse(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        message=request.POST.get("message")
        source=request.POST.get("source")
        Report.objects.create(name=name,email=email,message=message,source=source)
    return render (request,"somethingelse.html")
def form(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        message=request.POST.get("message")
        source=request.POST.get("source")
        Report.objects.create(name=name,email=email,message=message,source=source)
        messages.success(request,"Your form is submit")
    return render (request,"form.html")
def logoutuser(request):
    if request.method=="POST":
        request.POST.get("button")
        logout(request)
        return redirect("/login")
    return render(request,"login.html")

