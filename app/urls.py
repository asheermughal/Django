from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path("",views.loginuser,name="empty"),
    path("home/",views.home,name="home"),
    path("report/",views.report,name="report"),
    path("scam/",views.scam,name="scam"),
    path("somethingelse/",views.somethingelse,name="somethingelse"),
    path("aboutus/",views.form,name="form"),
    path("login/",views.loginuser,name="loginuser"),
    path("signup/",views.signup,name="signup"),
    path("logout/",views.logoutuser,name="logout"),
    path("forget/",views.forget,name="forget")

]