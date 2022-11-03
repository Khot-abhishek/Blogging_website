from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth.models import User
from django.views import View
from django.contrib import messages


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
            username = form.validated_data.get('username')
            messages.success(request, f"Account for '{username}' Successfully created! ")
            return redirect('login')
        else:
            messages.error(request, "Invalid input!, Please fill the correct info")
            return redirect('register')