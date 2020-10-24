from django.shortcuts import render
from .models import *
from random import *
from .utils import *
# Create your views here.
def IndexPage(request):
    return render(request,"app/index.html")

def LoginPage(request):
    return render(request,"app/login.html")

def registerUser(request):
    if request.POST['role'] == "employee":
        role = request.POST['role']
        email = request.POST['email']
        print("Email-------------------->",email)
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        gender = request.POST['gender']
        contact = request.POST['contact']

        user = User.objects.filter(email=email)
        if user:
            message = "User already Exist"
            return render(request,"app/index2.html",{'msg':message})
        else:
            if password == cpassword:
                otp = randint(10000,99999)
                newuser = User.objects.create(email = email,password=password,otp=otp,role=role)
                newemp = Employee.objects.create(user_id=newuser,Firstname = firstname,Lastname=lastname,gender=gender,contact=contact)
                email_Subject = "Employee Verifaction"
                sendmail(email_Subject,'mail_template',email,{'name':firstname,'otp':otp})
                return render(request,"app/login.html")
            else:
                message = "Password doesNot Match"
                return render(request,"app/index2.html",{'msg':message})
    else:
        print("Hirer Coming soon")


def LoginUser(request):
    if request.POST['role']=="employee":
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.get(email=email)
        if user:
            if user.password == password and user.role == "employee":
                emp = Employee.objects.get(user_id=user)
                request.session['email'] = user.email
                request.session['firstname'] = emp.Firstname
                return render(request,"app/home.html")


