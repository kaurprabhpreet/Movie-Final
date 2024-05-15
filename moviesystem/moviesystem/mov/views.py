from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request)
        if form.is_valid():
         user = form.save()
         login(request,user)
         return "success"
    else:
       form = UserCreationForm(request)
    return render(request, 'register.html', {'form':form})

def login(request):
   pass

def logout(request):
   pass