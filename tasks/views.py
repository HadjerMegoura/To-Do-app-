from django.shortcuts import render
from django.http import HttpResponse 
from .models import *

# Create your views here.
def index(request):
    notes = Note.objects.all()
    context = {'notes' : notes}
    return render(request,'tasks/index.html',context)
