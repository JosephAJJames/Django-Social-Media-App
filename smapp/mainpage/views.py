from django.shortcuts import render
from posts.forms import NewPostForm
from posts.models import Post


# Create your views here.
def post_list(req):
    posts = Post.objects.all()
    print(posts)

    for x in posts:
        print(x.text)

    return render(req, 'mainpage/main.html',
        context={
        'new_post_form': NewPostForm,
        'posts': posts
    })