from django.shortcuts import render, redirect

from blogs.models import BlogPost, Comment
from .forms import PostForm, CommentForm

from django.contrib.auth.decorators import permission_required


def index(request):
    """The home page for Blog."""
    return render(request, 'blogs/index.html')

def posts(request):
    """Show all the posts."""
    posts = BlogPost.objects.all().order_by('-date_added')
    context = {
        'posts': posts
    }
    return render(request, 'blogs/posts.html', context)

def post(request, post_id):
    """Show a post."""
    post = BlogPost.objects.get(id=post_id)

    context = {
        'post': post,
    }
    
    return render(request, 'blogs/post.html', context)

def comments(request, post_id):
    """Show comments to a post."""
    post = BlogPost.objects.get(id=post_id)
    comments = post.comment_set.order_by('-date_added')

    context = {
        'post': post,
        'comments': comments,
    }

    return render(request, 'blogs/comments.html', context)

@permission_required("blogs.add_post")
def new_post(request):
    """Add a new post."""
    if request.method != "POST":
        # No data submitted; create a blank form.
        form = PostForm()
    else:
        # POST data submitted; process data.
        form = PostForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("blogs:posts")
    
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)


def new_comment(request, post_id):
    """Add a new comment."""
    if request.method != "POST":
        # No data submitted, create a blank form
        form = CommentForm()
    else:
        # POST data submitted; process data.
        form = CommentForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("blogs:comments")

    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'blogs/new_comment.html', context)
