from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .models import Registration,Userlogin
from django.utils.timezone import now
# Create your views here.
def index(request):
    return render(request,'mainpage.html')


def contact_us(request):
    return render(request,"contact_us.html")


def about_us(request):
    return render(request,'about_us.html')


class login(View):
    def get(self,request):
     return render(request,"login.html")
    def post(self,request):
        usr=request.POST.get('un')
        psrd=request.POST.get('psd')
        try:
            Registration.objects.get(username=usr,password=psrd)
            Userlogin(uusername=usr,password=psrd).save()
            return render(request,"home.html",{"data":Userlogin.objects.all(),"name":usr,"dat":Registration.objects.all()})
        except:
            messages.error(request,"u dont have permission to login...so please go and register first!!!!!!!!(or) PLEASE CHECH U R PASSWORD!!!")
            return redirect('login')


class registration(View):
    def get(self,request):
        return render(request,"registration.html")
    def post(self,request):
      urname=request.POST.get('un')
      address=request.POST.get('adrs')
      email=request.POST.get('email')
      contactno=request.POST.get('contactno')
      password=request.POST.get('psd')
      Registration(username=urname,address=address,email=email,contactno=contactno,password=password).save()
      return render(request,"registration.html",{"message":"REGISTARED SUCCESSFULLY!!!!!!!!!!!!"})


def logout(request):
    pno=request.GET['uid']
    Userlogin.objects.filter(uid=pno).update(end_time=now())
    return render(request,"login.html")


def view_details(request):
    pno=request.GET.get('rid')
    res=Registration.objects.filter(rid=pno)
    return render(request,"view_details.html",{"dat":res})


def home(request):
    return render(request,"home.html")