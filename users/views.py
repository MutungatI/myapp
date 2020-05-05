from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method== 'POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'account created successfully  {username}')
            return redirect('login')


    else:
        form=UserRegisterForm()
    return render(request,'users/register.html',{'form':form})


@login_required
def profile(request):
    if request.method=='POST':
        u_update = UserUpdateForm(request.POST, instance=request.user)
        p_update = ProfileUpdateForm(request.POST, request.FILES,instance=request.user.profile)
        if u_update.is_valid and p_update.is_valid:
            u_update.save()
            p_update.save()
            messages.success(request, f'Info updated successfully')
            return redirect('profile')
    else:
        u_update = UserUpdateForm(request.POST, instance=request.user)
        p_update = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
    context={
        'u_form':u_update,
        'p_form':p_update,
        'title':request.user.username
    }
    return render(request,'users/profile.html',context)
