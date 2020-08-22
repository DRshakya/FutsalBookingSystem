from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


def feedback(request):
   feedback_page = loader.get_template("../ui/feedback.html")
   context = {}
   if "login_user" in request.session:
      context["login_user"] = request.session["login_user"]
      feedback_page = loader.get_template("../ui/feedback.html")
   return HttpResponse(feedback_page.render(context, request))

