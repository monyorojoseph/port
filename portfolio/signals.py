from django.db.models.signals import pre_save
from django.template.defaultfilters import slugify
from .models import Post


# recursive to get unique slug
def create_slug_recursion(instance, new_slug=None):
        slug = slugify(instance.title)
        klass = instance.__class__
        if klass.objects.filter(slug=slug).exists():
            return create_slug_recursion(instance, new_slug=slug)
        instance.slug = slug
        instance.save()
        return instance

# create post title slug
def create_post_slug(sender, instance, *args, **kwargs):
    if instance is None:
        create_post_slug(instance)

pre_save.connect(create_post_slug ,sender=Post)