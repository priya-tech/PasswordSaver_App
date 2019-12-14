from django import forms
from django.forms import ModelForm
from .models import AddPasswordModel

class AddPasswordForm(ModelForm):
    class Meta:
        model=AddPasswordModel
        fields=['name','password']
