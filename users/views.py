from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method != 'POST':
        form = RegisterForm()

    else:
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.is_active=False
            new_user.save()
            messages.success(request, 'Registration success on going admin verification')
            return redirect('mysites:index')
        
    context = {'form': form}
    return render(request, 'registration/register.html', context)

   # if form.is_valid():
    #        new_user = form.save()
    #        login(request, new_user)
    #        return redirect('mysites:index')

@login_required
def activate_acc(response, pk):
    if response.user.is_superuser:
        user = User.objects.get(id=pk)
        if response.method == 'POST':
            user.is_active=True
            user.save()
            return redirect('mysites:client')

        context = {'user': user}
        return render(response, 'mysites/activate.html', context)
    else:
        return redirect('mysites:index')

@login_required
def activate_dec(response, pk):
    if response.user.is_superuser:
        user = User.objects.get(id=pk)
        if response.method == 'POST':
            user.is_active=False
            user.save()
            return redirect('mysites:client')

        context = {'user': user}
        return render(response, 'mysites/activate.html', context)
    else:
        return redirect('mysites:index')


