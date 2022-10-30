from django.contrib import admin
from django.urls import path
from . import loginviews
urlpatterns = [
    path('login/',loginviews.loginpage,name="login")
]