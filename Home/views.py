from django.shortcuts import render , HttpResponse

# Create your views here.
from datetime import datetime 
from Home.models import Contact 

def index(request):
    context = {
        'role' : "Backend Engineer "
    }
    return render(request,'index.html' , context)

def contact(request):
    if request.method == "POST":
        data = request.POST.dict()
        name = data.get('name')
        phone = data.get('phone')
        message = data.get('message')
        email = data.get('email')
        contact = Contact(name=name,phone=phone,message=message,email=email,date=datetime.today())
        contact.save()
        # print(name,email,phone,message)
        # return render(request,'base.html')
    return render(request,'contact.html' )

def about(request):
    return render(request,'about.html' )

def services(request):
    return render(request,'services.html')