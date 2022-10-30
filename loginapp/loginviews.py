from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse 
import mysql.connector as sql
# Create your views here.

em = ""
pa = ""
@csrf_exempt
def loginpage(request):
    global em,pa
    if request.method == "POST":
        con = sql.connect(host="localhost",user = "root",passwd = "", database = "register")
        c = con.cursor()
        d = request.POST
        for key,value in d.items():
            if key == "email":
                em = value
            if key == "pass":
                pa = value
        r = "select * from userdetails where email='{}' and passw='{}'".format(em,pa)
        c.execute(r)
        t =tuple(c.fetchall())
        if t==():
            return render (request, 'error.html')
        else:
            return render(request, "welcome.html")
    return render(request, 'home.html')