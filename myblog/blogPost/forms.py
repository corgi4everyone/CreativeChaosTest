from django import forms
from django.contrib.auth import models
from django.db.models.base import Model
from django.forms import ModelForm, fields,widgets
from .models import Post,Catagory

class CreatePostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control', }),
            'title_tag':forms.TextInput(attrs={'class':'form-control', }),
            'catagory':forms.CheckboxSelectMultiple(),
            'author':forms.Select(attrs={'class':'form-control', }),
            'body' : forms.Textarea(attrs={'class':'form-control'})
        }
        

class CreateCatagoryForm(ModelForm):
    class Meta:
        model = Catagory
        fields='__all__'