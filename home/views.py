from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
from services.blog_service import BlogService


def index(request):
    topics = ["Computer Science", "Programming", "Database"]
    context = {
        'title': "Welcome to NCCS BLOG.",
        'topics': topics
    }
    if "login_user" in request.session:
        context["login_user"] = request.session["login_user"]
    index_page = loader.get_template("../ui/index.html")
    return HttpResponse(index_page.render(context, request))


def about(request):
    return HttpResponse("This is about page.")