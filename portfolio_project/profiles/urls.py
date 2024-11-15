from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page URL
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='profiles/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),  # Logout view URL
    path('profile/', views.profile, name='profile'),  # Profile page URL
    path('accounts/profile/', views.profile, name='profile'),  # Handling /accounts/profile/
    path('projects/', views.project_showcase, name='project_showcase'),  # Your project showcase URL
    path('add_project/', views.add_project, name='add_project'),  # Add project URL
]
