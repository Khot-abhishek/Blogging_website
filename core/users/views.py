from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth.models import User
from django.views import View
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView


def home(request):
    return render(request, 'users/home.html')




class RegistrationView(View):
    def get(self, request):
        context = {
            'form': RegistrationForm(),
        }
        return render(request, 'users/registration.html', context)
    
    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account for '{username}' Successfully created! ")
            return redirect('login')
        else:
            messages.error(request, "Invalid input!, Please fill the correct info")
            return redirect('register')

class UserLogin(LoginView):
    template_name = 'users/login.html'
    success_url = 'home'
    
    
class UserLogout(LogoutView):
    template_name = 'users/logout.html'       