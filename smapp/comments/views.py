from django.shortcuts import render

# Create your views here.
def new_comment(req):
    if req.method == "POST":
        form = CommentForm(req.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = req.user
            comment.post = get_object_or_404(Post, pk=req.POST.get("post_id"))
            form.save()