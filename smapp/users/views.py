from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import login
from .forms import UserForm

# Create your views here.

def login_user(req):
    if req.method == "GET":
        return render(req, 'users/login_page.html',
        context={
            'login_form': AuthenticationForm
        })

    elif req.method == "POST":
       form = AuthenticationForm(data=req.POST)
       if form.is_valid():
            print(req.POST.get("email"))
            print(req.POST.get("username"))
            print(req.POST.get("password"))
            login(req, form.get_user())
            print("logged in")
            return HttpResponse("logged in")
       return HttpResponse("not worked")