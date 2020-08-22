from django.urls import path

from . import views

urlpatterns = [
    path('new/', views.index, name='newblog'),
    path('delete/', views.delete_blog, name='deleteblog'),
]