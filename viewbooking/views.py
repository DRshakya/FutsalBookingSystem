from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


def user(request):
   userbooking_page = loader.get_template("../ui/viewbookinguser.html")
   context = {}
   if "login_user" in request.session:
      context["login_user"] = request.session["login_user"]
      userbooking_page = loader.get_template("../ui/viewbookinguser.html")
   return HttpResponse(userbooking_page.render(context, request))

def admin(request):
   context = {}
   if "login_user" in request.session:
      context["login_user"] = request.session["login_user"]
      adminbooking_page = loader.get_template("../ui/viewbookingadmin.html")
   return HttpResponse(adminbooking_page.render(None, request))
