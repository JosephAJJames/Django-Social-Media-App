from django.http import HttpResponse
from django.shortcuts import render
from .forms import NewPostForm

# Create your views here.
def new_post(req):
    if req.method == "POST":
        form = NewPostForm(req.POST, req.FILE)
        return HttpResponse("post recieved")