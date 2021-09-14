from django import forms
from django.shortcuts import render,redirect
from .models import Catagory, Post
from .forms import CreatePostForm, CreateCatagoryForm

# Create your views here.
def home(request):
    posts = Post.objects.all()
    tags = Catagory.objects.all()
    featured_post = Post.objects.last()
    return render(request,'blogpost/index.html', {'posts':posts, 'featured_post':featured_post, 'tags':tags})

def postDetail(request,pk):
    post = Post.objects.get(id=pk)
    tags = Catagory.objects.all()
    context = {'post':post, 'tags':tags}
    return render(request,'blogpost/post_detail.html',context)


def createPost(request):
    form = CreatePostForm()
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request,'blogpost/post_form.html', context)

def deletePost(request,pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('home')

    context = {'post':post}
    return render(request,'blogpost/delete_post.html', context)

def updatePost(request,pk):
    post = Post.objects.get(id=pk)

    form = CreatePostForm(instance=post)

    if request.method == 'POST':
        form= CreatePostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')

    context={'form':form}
    return render(request,'blogpost/post_form.html',context)

def createCatagory(request):
    form = CreateCatagoryForm()
    if request.method == 'POST':
        form = CreateCatagoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request,'blogpost/catagory_form.html',context)

def catagoryPage(request,pk):
    cag =  Catagory.objects.get(name=pk)
    catagory_posts = Post.objects.filter(catagory= cag.id)
    tags = Catagory.objects.all()
    context = {
        'catagory_posts':catagory_posts,
        'cag':cag,
        'tags':tags,
    }
    return render(request,'blogpost/catagory_page.html',context)

