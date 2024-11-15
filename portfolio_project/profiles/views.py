from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import SignupForm, ProfileForm, ProjectForm
from django.contrib.auth.decorators import login_required
from .models import Profile, Project

# Home page view
def home(request):
    return render(request, 'profiles/home.html')

# Signup view for user registration
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # Redirect to profile page after successful signup
            return redirect('profile')
    else:
        form = SignupForm()
    return render(request, 'profiles/signup.html', {'form': form})

# Profile view to manage the user's profile (bio, skills, contact info)
@login_required
def profile(request):
    user_profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=user_profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('profile')
    else:
        profile_form = ProfileForm(instance=user_profile)

    return render(request, 'profiles/profile.html', {'profile_form': profile_form})

# View to log the user out and redirect to home page
def logout_view(request):
    logout(request)
    return redirect('home')

# View to add a new project to the user's portfolio
@login_required
def add_project(request):
    if request.method == 'POST':
        project_form = ProjectForm(request.POST, request.FILES)
        if project_form.is_valid():
            project = project_form.save(commit=False)
            project.user = request.user  # Associate the project with the current user
            project.save()
            return redirect('project_showcase')  # Redirect to project showcase page after adding a project
    else:
        project_form = ProjectForm()

    return render(request, 'profiles/add_project.html', {'project_form': project_form})

# View to showcase all projects added by the user (Project Showcase)
@login_required
def project_showcase(request):
    # Get all projects associated with the logged-in user
    projects = Project.objects.filter(user=request.user)
    return render(request, 'profiles/project_showcase.html', {'projects': projects})
