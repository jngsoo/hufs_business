from django.shortcuts import render, redirect, render_to_response
from .forms import SigninForm
from .models import Origin_users
from django.contrib.auth.models import User
from django.contrib.auth import login

from django.db.models import Q

from django.contrib import messages



def signin(request):
    num = request.POST.get('user_number')
    pd1 = request.POST.get('user_password')
    pd2 = request.POST.get('user_password2')

    if request.method == "POST":
        form = SigninForm(request.POST)
        if form.is_valid():
            if Origin_users.objects.filter(origin_number=num) and (pd1 == pd2):
                form.save()
                return redirect('/')
            elif(not Origin_users.objects.filter(origin_number=num)):
                pass
            elif((pd1 != pd2)):
                pass
            else:
                return redirect('/')
    else:
        form = SigninForm()
        return render(request, 'joining.html', {'form': form,})

   