from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def showDemoPage(request):
    return render(request,'demo.html')


def showLoginPage(request):
    return render(request,'login_page.html')


def doLogin(request):
    if request.method !="POST":
        return HttpResponse("method not allowed")
    
    else:
        return HttpResponse("Email: "+request.POST.get("email")+" Password: "+request.POST.get("password"))
    