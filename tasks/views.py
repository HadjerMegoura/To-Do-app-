from django.shortcuts import redirect, render
from django.http import HttpResponse 
from .models import *
from .forms import *

# Create your views here.
def index(request):
    form = NoteForm()
    notes = Note.objects.all()

    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid() :
            form.save()
        return redirect('/')

    context = {'notes' : notes, 'form':form}
    return render(request,'tasks/index.html',context)

def update(request,pk):
    task = Note.objects.get(id=pk)
    form = NoteForm(instance=task)

    if request.method == 'POST':
        form = NoteForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request,'tasks/update.html',context)

def delete(request,pk):
    task = Note.objects.get(id=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('/')
    context ={'task':task}
    return render(request,'tasks/delete.html',context)
