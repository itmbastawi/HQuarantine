from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from ..forms import profile_form


@login_required
def ask_service(request):
    user_id =request.user
    return render(request,'order/ask_service.html',{})


@login_required
def profile(request):
    user = request.user.user_profile

    form = profile_form(instance=user)
    user_id =request.user
    contex = {'form':form}
    return render(request,'order/profile.html',contex)
