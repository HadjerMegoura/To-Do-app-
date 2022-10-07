import imp
from pyexpat import model
from django import forms
from django.forms import ModelForm
from .models import *

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'
