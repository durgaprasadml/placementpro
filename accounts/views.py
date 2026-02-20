from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import LoginForm, RegisterForm
from .models import UserProfile


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user, role=form.cleaned_data['role'])
            messages.success(request, 'Registration successful. Please login.')
            return redirect('accounts:login')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('accounts:role_redirect')
    else:
        form = LoginForm(request)
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('accounts:login')


@login_required
def role_redirect(request):
    role = request.user.profile.role
    if role == UserProfile.Role.STUDENT:
        return redirect('students:dashboard')
    if role == UserProfile.Role.TPO:
        return redirect('drives:tpo_dashboard')
    if role == UserProfile.Role.ALUMNI:
        return redirect('alumni:dashboard')
    messages.error(request, 'Role is not configured for this account.')
    return redirect('accounts:login')
