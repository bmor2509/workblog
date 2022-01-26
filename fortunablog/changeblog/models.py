from django.db import models
# import to import the superuser model 
from django.contrib.auth.models import User
from django.db.models.deletion import SET_DEFAULT
# Create your models here.
# import reverse for URL redirects after form submissions
from django.urls import reverse
from datetime import datetime, date




class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name 

    def get_absolute_url(self):
        return reverse('home')

class Site(models.Model):
    site = models.CharField(max_length=255)

    def __str__(self):
        return self.site

    def get_absolute_url(self):
        return reverse('home')

class Visibility(models.Model):
    visibility = models.CharField(max_length=255)

    def __str__(self):
        return self.visibility

    def get_absolute_url(self):
        return reverse('home')

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default='ppc')
    site = models.CharField(max_length=255, default='King Casino')
    visibility = models.CharField(max_length=255, default='Public')

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')