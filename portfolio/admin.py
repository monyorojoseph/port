from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group

# Register your models here.

admin.site.unregister(Group)
admin.site.register(Project)
admin.site.register(Stack)
admin.site.register(Post)

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['email_address', 'twitter_url', 'github_url']

    def has_add_permission(self, request) -> bool:
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)