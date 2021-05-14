from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from .models import Register


# Create your views here.
def first(request):
    return render(request,'first.html')
def second(request):
    return render(request,'second.html')
def third(request):
    return render(request,'third.html')
def new(request):
    return render(request,'new.html')
def email(request):
    send_mail('Hello','how is it going?','dhaneshwaran96@gmail.com',['dhaneshwaranvl@gmail.com'])
    return HttpResponse('email sent successfully')


def register(request):

    return render(request,'register.html')


def insert(request):

    if(request.method=='POST'):

        obj = Register()

        obj.Name = request.POST.get('username')

        obj.Password = request.POST.get('userpass')

        obj.Age = request.POST.get('userage')
        obj.Address = request.POST.get('useraddress')
        obj.Phone = request.POST.get('userphone')

        obj.save()

        return render(request,'insert.html')

    else:

        return render(request,'register.html')

def showRecord(request):
    data = Register.objects.all()
    context = {'result':data}

    return render(request,'showRecord.html',context)


    