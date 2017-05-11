from django.contrib import admin
from django.db import models
from admin_extends.widgets import AdminImageWidget
from .models import Post, Image


class ImageAdmin(admin.TabularInline):
    model = Image
    extra = 2

    def __init__(self, *args, **kwargs):
        super(ImageAdmin, self).__init__(*args, **kwargs)
        self.formfield_overrides.update({models.ImageField: {'widget': AdminImageWidget}})


class PostAdmin(admin.ModelAdmin):
    inlines = [ImageAdmin]


admin.site.register(Post, PostAdmin)
