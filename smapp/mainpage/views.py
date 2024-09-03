from django.shortcuts import render
from posts.forms import NewPostForm
from comments.forms import CommentForm
from posts.models import Post
from comments.models import Comment


# Create your views here.
def post_list(req):
    posts = Post.objects.all()
    comments = Comment.objects.all()

    return render(req, 'mainpage/main.html',
        context={
        'new_post_form': NewPostForm,
        'new_comment_form': CommentForm,
        'posts': posts
    })