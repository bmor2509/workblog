from django import forms
from django.db.models import fields
from django.db.models.expressions import Value 
from .models import Post, Category, Site, Visibility

choices = Category.objects.all().values_list('name', 'name')
site_choices = Site.objects.all().values_list('site', 'site')
visibility = Visibility.objects.all().values_list('visibility', 'visibility')



choice_list = []
site_choice_list=[]
visibility_list=[]

for item in choices:
    choice_list.append(item)

for item in site_choices:
    site_choice_list.append(item)

for item in visibility:
    visibility_list.append(item)

class PostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].disabled = True

    class Meta:
        model=Post
        fields = ('title', 'author', 'category', 'site', 'body', 'visibility')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control' ,'readonly': 'readonly'}),
            'category': forms.Select(choices=choice_list,attrs={'class': 'form-control'}),
            'site': forms.Select(choices=site_choice_list,attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'visibility': forms.Select(choices=visibility_list,attrs={'class': 'form-control'})
        }

class EditForm(forms.ModelForm):
    class Meta:
        model=Post
        fields = ('title', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'})
        }