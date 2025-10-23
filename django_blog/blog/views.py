from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, ProfileForm


# Create your views here.

def register(request): # registration of new user
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def profile_view(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
        else:
            form = ProfileForm(instance=profile)
            return render(request, blog/profile.html, {'form': form})