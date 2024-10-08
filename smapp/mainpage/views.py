from django.shortcuts import render
from posts.forms import NewPostForm
from comments.forms import CommentForm
from posts.models import Post
from comments.models import Comment


# Create your views here.
def post_list(req):
    posts = Post.objects.all()
    comments = Comment.objects.all()
    comment_dict = {}

    comment_forms = []
    for post in posts:
        new_comment = CommentForm(initial={'post_id': post.id})
        comment_forms.append(new_comment)

    comments = Comment.objects.all()

    for y in comments:
        if y.post_id.id not in comment_dict:
            comment_dict[y.post_id.id] = [y]
        else:
            comment_dict[y.post_id.id].append(y)


    posts_with_forms = zip(posts, comment_forms)

    print(comment_dict)


    return render(req, 'mainpage/main.html',
                  {'new_post': NewPostForm,
                   'posts': posts,
                   'posts_and_comment_form': posts_with_forms,
                   'comment_dict': comment_dict
                   })