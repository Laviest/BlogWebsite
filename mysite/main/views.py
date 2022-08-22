from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog
from .forms import BlogForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='login')
def home(request):
    blog_list = Blog.objects.all()

    if request.method == "POST":
        blog_id = request.POST.get("blog-id-delete")
        blog = Blog.objects.filter(id=blog_id).first()
        if blog and blog.user == request.user:
            blog.delete()

    blog_length = len(request.user.blog_search.all())

    return render(request, 'main/home.html', {'blog_list': blog_list, 'blog_length': blog_length})


@login_required(login_url='login')
def create_blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            request.user.blog_search.add(post)

            return redirect('home')
    else:
        form = BlogForm()

    context = {'form': form}

    return render(request, 'main/create_blog.html', context)


@login_required(login_url='login')
def update_blog(request):
    form = BlogForm()
    context = {'form': form}
    return render(request, 'main/create_blog.html', context)


@login_required(login_url='login')
def my_profile(request):
    blog_list = Blog.objects.all()

    if request.method == "POST":
        blog_id = request.POST.get("blog-id-delete")
        blog = Blog.objects.filter(id=blog_id).first()
        if blog and blog.user == request.user:
            blog.delete()

    blog_length = len(request.user.blog_search.all())
    context = {'blog_list': blog_list, 'blog_length': blog_length}

    return render(request, 'main/my_profile.html', context)


def edit_blog(request, id):
    blog = Blog.objects.get(id=id)
    if blog.user == request.user:
        form = BlogForm(request.POST or None, request.FILES or None, instance=blog)

        if form.is_valid():
            form.save()
            return redirect('my_profile')
    else:
        return redirect('home')

    return render(request, 'main/edit.html', {'blog_id': blog, 'form': form})


def view_other_profile(request, id):
    user = User.objects.get(id=id)
    blog_length = len(user.blog_search.all())

    return render(request, 'main/other_profile.html', {'user': user, 'blog_length': blog_length})

