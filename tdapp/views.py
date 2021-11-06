from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.


def home(request):
    record=Records.objects.all()
    
    context={'record':record}
    return render(request,'home.html',context)

def add(request):
    form=RecordsForm()
    if request.method=='POST':
        form=RecordsForm(request.POST)
        if form.is_valid():
            form.save()
        
        return redirect('/',{'form':form}) 
    return render(request,'add.html')

def edit(request,x):
    record=Records.objects.get(id=x)
    
    return render(request,'edit.html',{'record':record})

def update(request,x):
    record=Records.objects.get(id=x)
    form = RecordsForm(request.POST,instance = record)
    if form.is_valid():  
        form.save()  
        return redirect("/home") 
    else: 
        return render(request, 'edit.html', {'form': form})

def erase(request,x): 
    record = Records.objects.get(id=x)  
    record.delete()  
    return redirect("/home")
            
    