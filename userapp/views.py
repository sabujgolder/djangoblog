from django.shortcuts import render,redirect
from .forms import userreg
from django.contrib import messages

def registeruser(request):

    if request.method == "POST":
        form = usereg(request.Post)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            message.success(request,f'User created for {username}!')
            return redirect('home')
    form = userreg()

    return render(request,'userapp/register.html',{'form':form})
