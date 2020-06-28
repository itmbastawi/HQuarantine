from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from ..forms import profile_form
from django.contrib import messages


@login_required
def ask_service(request):
    user_id =request.user
    return render(request,'order/ask_service.html',{})


@login_required
def profile(request):
    if request.method == 'POST':
        form = profile_form(request.POST,
                            request.FILES,
                            instance=request.user.user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile Update !')
        return redirect('index')
    else :
        user = request.user.user_profile
        form = profile_form(instance=user)
    
    contex = {'form':form}
    return render(request,'order/profile.html',contex)
