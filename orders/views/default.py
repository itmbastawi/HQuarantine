from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from ..models import user_profile

# Create your views here.
def index(request):
    order = request.user.groups.filter(name='order').exists()
    if order:
        return redirect('askService')
    return render(request,'default/index.html',{'group':order})

def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            p = user_profile.objects.create(user_id=user)
            p.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('index')
        else:
            messages.error(request,form.errors)
    else:
        form = UserCreationForm()

    return render(request,'default/registration.html',
                    {'form':form})


