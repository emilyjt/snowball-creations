from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, CompanyUpdateForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to login!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        c_form = CompanyUpdateForm(request.POST, instance=request.user.userprofile.company)
        if u_form.is_valid() and p_form.is_valid() and c_form.is_valid():
            u_form.save()
            p_form.save()
            c_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.userprofile)
        c_form = CompanyUpdateForm(instance=request.user.userprofile.company)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'c_form': c_form,
    }

    return render (request, 'users/profile.html', context)


# #types of messages
# message.debug
# message.info
# message.success
# message.warning
# message.error
