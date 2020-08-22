from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


def about(request):
   about_page = loader.get_template("../ui/about.html")
   context = {}
   if "login_user" in request.session:
      context["login_user"] = request.session["login_user"]
      about_page = loader.get_template("../ui/about.html")
   return HttpResponse(about_page.render(context, request))
