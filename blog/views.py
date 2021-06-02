from django.shortcuts import render, HttpResponse, redirect
from blog.models import Post, BlogComment
from django.contrib import messages

# Create your views here.
def blogHome(request):
    allpost = Post.objects.all()
    context = {'allpost': allpost}
    return render(request, 'blog/blog.html', context)
    
def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    comments = BlogComment.objects.filter(post=post)
    context = {"post": post, "comments":comments, 'user':request.user}
    return render(request, 'blog/blogpost.html', context)

def postComment(request):
    if request.method == 'POST':
        comment = request.POST.get("comment")
        user = request.user
        postSno = request.POST.get("postSno")
        post = Post.objects.get(Sno=postSno)
        parentSno = request.POST.get("parentSno")
        if parentSno == "":
            comments = BlogComment(comment=comment, user=user, post=post)
            comments.save()
            messages.success(request, "Your comment has been posted.")
        else:
            parent=BlogComment.objects.get(sno=parentSno)
            comments = BlogComment(comment=comment, user=user, post=post, parent=parent)
            comments.save()
            messages.success(request, "Your reply has been posted.")
    return redirect(f"/blog/{post.slug}")