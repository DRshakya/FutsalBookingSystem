from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from django.core.files.storage import FileSystemStorage

import os

# Create your views here.
from models.blog import Blog
from models.user import User
from models.user_register import UserRegister
from services.account_service import AccountService
from services.blog_service import BlogService


def delete_blog(request):
    if request.POST and "login_user" in request.session:
        blog_id = request.POST["txtBlogId"]
        blog_service = BlogService()
        blog_service.delete(blog_id)
    return redirect("index")

def index(request):
    index_page = loader.get_template("../ui/blog.html")
    context = {}
    if "login_user" in request.session:
        context["login_user"] = request.session["login_user"]
        if request.POST:
            title = request.POST["txtTitle"]
            tag = request.POST["txtTags"]
            body = request.POST["txtBlog"]
            blog = Blog()
            blog.title = title
            blog.tag = tag
            blog.body = body
            if request.FILES and "blogImage" in request.FILES:
                blog_image = request.FILES["blogImage"]
                fs = FileSystemStorage()
                path = os.path.join("static/uploads", blog_image.name)
                saved_file = fs.save(path, blog_image)
                file_path = fs.url(saved_file)
                blog.blog_image = file_path
            blog.user = request.session["login_user"]
            context["blog"] = blog
            if not title:
                context["error_msg"] = "Invalid title"
            elif not tag:
                context["error_msg"] = "Invalid tag"
            elif not body:
                context["error_msg"] = "Blog body can't be empty."
            else:
                blog_service = BlogService()
                result = blog_service.save(blog)
                if result is None:
                    context["error_msg"] = "Could not save blog."
                else:
                    del context["blog"]
                    context["success_msg"] = "Blog saved successfully."
    else:
        return redirect("signin")
    return HttpResponse(index_page.render(context, request))