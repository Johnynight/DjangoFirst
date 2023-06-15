from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import UserRegistrationForm, Form, ProfileForm

from django.contrib.auth import logout
from django.shortcuts import redirect
from .models import Profile


def logout_view(request):
    logout(request)
    return redirect('home')  # Замените 'home' на URL-шаблон вашей домашней страницы


# Create your views here.


def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})


@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = Form(instance=request.user, data=request.POST)
        profile_form = ProfileForm(instance=request.user.profile, data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('/blog/')
    else:
        user_form = Form(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
        context = {
            'user_form': user_form,
            'profile_form': profile_form,
        }
    return render(request, 'account/profile_form.html', context)
