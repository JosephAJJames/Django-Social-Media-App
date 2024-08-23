from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login

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
            login(req, form.get_user())
            return redirect("mainpage:post_list")
       return HttpResponse("not worked")


def register_user(req):
    if req.method == "GET":
        return render(req,
        'users/sign_up.html',
        context={
            'signup_form': UserCreationForm
        })