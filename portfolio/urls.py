from django.urls import path
from .views import *

app_name = "portfolio"

urlpatterns = [
    path("", home, name="home"),
    path("posts/", posts, name="posts"),
    path("post/<slug:slug>", post_details, name="post-details"),
    path("projects/", projects, name="projects"),
    path("project/<int:id>", project_details, name="project-details")
]
