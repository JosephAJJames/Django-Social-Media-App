from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserForm

# Create your views here.

def login(req):
    if req.method == "GET":
        return render(req, 'users/login_page.html',
        context={
            'login_form': UserForm
        })

    elif req.method == "POST":
       form = UserForm(req.POST)
       if form.is_valid():
            print(req.POST.get("email"))
            print(req.POST.get("username"))
            print(req.POST.get("password"))
            return HttpResponse("form received")