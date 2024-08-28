from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import NewPostForm

# Create your views here.
def new_post(req):
    if req.method == "POST":
        form = NewPostForm(req.POST, req.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = req.user
            print("saved")
            form.save()
            return redirect("mainpage:post_list")
        else:
            return HttpResponse("not valid")