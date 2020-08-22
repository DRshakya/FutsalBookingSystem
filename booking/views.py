from django.core import serializers

from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import redirect
from datetime import date, datetime

from repo.book_repo import BookRepo


def book(request):

   booking_page = loader.get_template("../ui/booking.html")
   context={}
   if "login_user" in request.session:
      context["login_user"] = request.session["login_user"]
      # user_id = request.session.get('login_user')
      user = request.session.get('login_user', 'default value')
      if request.POST:
         date1 = request.POST["txtdate"]
         starttime = int(request.POST["starttime"])
         endtime = int(request.POST["endtime"])
         cmp = endtime-starttime
         ground = request.POST["ground"]
         d1 = datetime.today().strftime("%Y-%m-%d")
         b_id = 100
         uid = user.user_id
         print(d1)
         print(date1)

         if cmp>1:
            context["invalid_msg"] = "Invalid Time!!!"
         elif starttime == endtime:
            context["invalid_msg"] = "Start and end cant be same"
         elif endtime < starttime:
            context["invalid_msg"] = "Invalid Time!!!"
         elif date1 < d1:
            context["invalid_msg"] = "Cant book on pssed date!!!"
         else:
             book_repo =BookRepo()
             result = book_repo.check_book(uid,date1, starttime, endtime, ground)
             if result is True:
                context["success_msg"] = "Sucessfully booked"
             else:
                context["error_msg"] = "Already Booked or Error in booking "

   return HttpResponse(booking_page.render(context, request))
