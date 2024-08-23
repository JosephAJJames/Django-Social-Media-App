from django.shortcuts import render

#returns home page
def home(req):
    if req.method == "GET":
        return render(req, 'smapp/home.html')
