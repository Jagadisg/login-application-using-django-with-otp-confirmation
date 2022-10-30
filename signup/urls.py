from django.contrib import admin
from django.urls import path
from . import signviews
urlpatterns = [
    path('login/signup/',signviews.signup,name="signup"),
    path('login/signup/verify',signviews.verify,name="verify")
]