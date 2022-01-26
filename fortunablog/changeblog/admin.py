from django.contrib import admin
from django.contrib.admin.sites import site
# Import the classes to register from models
from .models import Post, Category, Site, Visibility
# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Site)
admin.site.register(Visibility)