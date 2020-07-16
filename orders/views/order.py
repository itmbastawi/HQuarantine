from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from ..forms import profile_form,item_form
from django.contrib import messages
from ..models import service_table

@login_required
def ask_service(request):
    items = service_table.objects.all()
    user =request.user
    if request.method == 'POST':
        form = item_form(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_user = user
            item.save()
            messages.success(request, 'Server added !')
        form.clean()
    else :
        form = item_form()
    return render(request,'order/ask_service.html',{'form':form,
                                                    'items':items})


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
