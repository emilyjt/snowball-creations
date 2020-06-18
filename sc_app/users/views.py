from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, CompanyUpdateForm
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
        user_form = UserUpdateForm(request.POST, instance=request.user)
        company_form = CompanyUpdateForm(request.POST, instance=request.user.userprofile.company)
        if user_form.is_valid() and company_form.is_valid():
            user_form.save()
            company_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        company_form = CompanyUpdateForm(instance=request.user.userprofile.company)

    context = {
        'user_form': user_form,
        'company_form': company_form,
    }

    return render (request, 'users/profile.html', context)


# #types of messages
# message.debug
# message.info
# message.success
# message.warning
# message.error
