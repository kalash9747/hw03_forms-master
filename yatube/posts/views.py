from .forms import PostForm
from django.shortcuts import get_object_or_404, redirect, render
from .models import Group, Post, User
from django.core.paginator import Paginator


def index(request):
    post_list = Post.objects.all().order_by('-pub_date')
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'index.html', {"page": page})


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    post_list = Post.objects.filter(group=group).order_by('-pub_date')
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, "posts/group.html", {"group": group, "page": page})


def profile(request, username):
    author = get_object_or_404(User, username=username)
    post_list = Post.objects.filter(author=author).order_by('-pub_date')
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'profile.html', {"author": author, "page": page})


def post_view(request, username, post_id):
    author = get_object_or_404(User, username=username)
    post = Post.objects.filter(author=author).get(id=post_id)
    return render(request, 'post.html', {"author": author, "post": post})


def new_post(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        form.save()
        return redirect('index')
    form = PostForm()
    return render(request, 'new_post.html', {'form': form})


def post_edit(request, username, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user != post.author:
        return redirect('post', username, post_id)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('post', username, post_id)
    form = PostForm()
    return render(request, 'new_post.html', {'form': form,
                                             'edit': True})
