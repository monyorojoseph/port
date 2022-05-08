from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.db import models
from django_quill.fields import QuillField


# Create your models here.

# blog
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    published = models.DateTimeField(auto_now_add=True)
    content = QuillField()

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return f"/post/{self.slug}"
    

# tech stack
class Stack(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:  
        return self.name
    
    class Meta:
        verbose_name_plural = "Stack"

# projects
class Project(models.Model):
    name = models.CharField(max_length=200, unique=True)
    cover_image = ProcessedImageField(upload_to='projects/',
                                           processors=[ResizeToFill(250, 150)],
                                           format='JPEG',
                                           options={'quality': 100})
    tech_stack = models.ManyToManyField(Stack)
    description = QuillField()
    link = models.URLField()

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return f"/project/{self.id}"

    def cover_image_url(self):
        return self.cover_image.url
    

class About(models.Model):
    image = models.ImageField(upload_to="about/")
    introduction = QuillField()
    content = QuillField()
    email_address = models.EmailField(max_length=200)
    twitter_url = models.CharField(max_length=200)
    discord_id = models.CharField(max_length=200)
    github_url = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "About"
    
    def get_image_url(self):
        return self.image.url