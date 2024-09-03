from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserForm
from profilepics.models import ProfilePic
from .helpers import detect_difference, apply_changes

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
            'signup_form': UserForm
        })
    elif req.method == "POST":
        form = UserForm(req.POST)

        if form.is_valid():
            user = form.save(commit=False)
            default_pic = ProfilePic.objects.get(is_default=True)
            user.profilepic_id = default_pic.id
            user.save()
        return redirect("users:login")


def edit_profile(req):
    if req.method == "GET":
        return render(req, 'users/edit_profile.html', context={
            'user': req.user
        })
    elif req.method == "POST":
        new_username, new_password, new_pfp = req.POST.get("username"), req.POST.get("password"), req.FILES.get("profilepic")
        current_user_dict, alterd_user_dict = {"username": req.user.username, "password": req.user.password, "profilepic": req.user.profilepic}, {"username": new_username, "password": new_password, "profilepic": new_pfp}

        differences = detect_difference(current_user_dict, alterd_user_dict) #will return a dict of the attributes to be changed and what to change to
        apply_changes(differences, req.user)

        return redirect("users:edit_profile")