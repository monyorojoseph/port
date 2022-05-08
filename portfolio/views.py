from multiprocessing import context
from django.shortcuts import render
from .models import Post, About, Project

# Create your views here.
def home(request):
    about = About.objects.all()[0]
    projects = Project.objects.all()[:3]
    posts = Post.objects.all()[:6]
    context = {
        "about":about,
        "projects": projects,
        "posts": posts
        }
    return render(request, 'portfolio/home.html', context )

# get posts
def posts(request):
    return render(request, "portfolio/posts.html", {"posts":Post.objects.all()})

# post details
def post_details(request, slug):
    return render(request, 'portfolio/post_detail.html', {"post":Post.objects.get(slug=slug)}) 

def projects(request):
    return render(request, 'portfolio/projects.html', {"projects": Project.objects.all()})

def project_details(request, id):
    return render(request, "portfolio/project_detail.html", {"project": Project.objects.get(pk=id)})