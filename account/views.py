from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect

# Create your views here.
from models.user import User
from models.user_register import UserRegister
from services.account_service import AccountService


def signout(request):
    request.session.flush()
    return redirect("signin")

def signin(request):
    index_page = loader.get_template("../ui/login.html")
    context = {}
    if request.POST:
        email = request.POST["txtEmail"]
        password = request.POST["txtPassword"]
        if not email:
            context["error_msg"] = "Invalid email or password."
        elif email=="admin@gmail.com" and password=="admin":
            user = User()
            user.user_id = 1001
            user.full_name = "Owner"
            user.email = "admin@gmail.com"
            request.session["login_user"] = user
            return redirect("index")
        else:
            account_service = AccountService()
            user = account_service.signin(email, password)
            if user is None:
                context["error_msg"] = "Invalid email or password."
            else:
                context["success_msg"] = "Logged in successfully."
                request.session["login_user"] = user
                return redirect("index")
    return HttpResponse(index_page.render(context, request))

def signup(request):
    index_page = loader.get_template("../ui/signup.html")
    context = {}
    if request.POST:
        full_name = request.POST["txtFullname"]
        email = request.POST["txtEmail"]
        address = request.POST["txtAddress"]
        phone = request.POST["txtPhone"]
        password = request.POST["txtPassword"]
        cpassword = request.POST["txtCPassword"]
        user_register = UserRegister()
        user = User()
        user.full_name = full_name
        user.email = email
        user.phone = phone
        user.address = address
        user_register.user = user
        user_register.password = password
        user_register.cpassword = cpassword
        context["user_register"] = user_register
        if not full_name or len(str(full_name).strip(' ')) <= 5:
            context["invalid_msg"] = "Invalid full name."
        elif not email or len(str(email).strip(' ')) <= 7:
            context["invalid_msg"] = "Invalid email."
        elif not password or len(str(password).strip(' ')) < 8:
            context["invalid_msg"] = "Invalid password. Must be 8 character long."
        elif not cpassword or password != cpassword:
            context["invalid_msg"] = "Password do not match."
        elif full_name == "Owner" or full_name =="owner":
            context["invalid_msg"] = "Full name cant be owner"
        else:
            account_service = AccountService()
            result_user = account_service.signup(user_register)
            if result_user is None:
                context["invalid_msg"] = "Could not save user."
            else:
                context["success_msg"] = "User registered successfully."
    return HttpResponse(index_page.render(context, request))