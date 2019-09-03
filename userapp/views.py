from django.shortcuts import render,redirect
from .forms import userreg
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def registeruser(request):

    if request.method == "POST":
        form = userreg(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'User created for {username}!')
            return redirect('login')
    form = userreg()

    return render(request,'userapp/register.html',{'form':form})

@login_required
def profile(request):
    return render(request,'userapp/profile.html')
