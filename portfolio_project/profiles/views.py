from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import SignupForm
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'profiles/home.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = SignupForm()
    return render(request, 'profiles/signup.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'profiles/profile.html')

def logout_view(request):
    logout(request)
    return redirect('home')  # Redirect to home page after logout
