from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.IndexPage,name="index"),
    path("register/",views.registerUser,name="register"),
    path("loginpage/",views.LoginPage,name="loginpage"),
    path("login/",views.LoginUser,name="login"),
]
