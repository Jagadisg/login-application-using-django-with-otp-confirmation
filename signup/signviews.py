from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import mysql.connector as sql
import random
import smtplib
# Create your views here.
us = ""
em = ""
pa = ""
ge = ""
otp = ""
@csrf_exempt
def signup(request):
    global us,em,pa,ge,otp
    if request.method == "POST":
        d = request.POST
        for key,value in d.items():
            if key == "user":
                us = value
            if key == "email":
                em = value
                server = smtplib.SMTP('smtp.gmail.com',587)
                server.starttls()
                otp = ''.join([str(random.randint(0, 9)) for i in range(4)])
                server.login("hisdagaj.CE@gmail.com","yehyngrhujhbekgb")
                msg = f"Dear {us}\n\nWelcome to our website\nFor email-id verfication otp is {otp}"
                server.sendmail('hisdagaj.CE@gmail.com', em, msg)
                server.quit()
            if key == "pass":
                pa = value
            if key == "gender":
                ge = value
        res = redirect('verify')
        return res
    return render(request, 'sign.html')

@csrf_exempt        
def verify(request): 
    if request.method == "POST":
        o = request.POST
        v = []
        for key,value in o.items():
            v.append(value)
        otp1 = ''.join(v[::-1])
        if otp == otp1:
            con = sql.connect(host="localhost",user = "root",passwd = "", database = "register")
            c = con.cursor()
            r = ("insert into userdetails values('{}','{}','{}','{}')").format(us,em,pa,ge)
            c.execute(r)
            con.commit()
            return render(request,'verify.html',{'mess': " EMAIL-ID SUCCESSFULLY VERFIED "})
            return render(request,'home.html')
        elif otp != otp1:
            return render(request,'verify.html', {'message':'WRONG OTP'})
    return render(request,'verify.html')    
                       
