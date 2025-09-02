from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View

class CustomLoginView(View):
    def get(self, request):
        return render(request, 'users/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me')  # checkbox name

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            # If remember me is not checked, session expires on browser close
            if not remember_me:
                request.session.set_expiry(0)  # Session expires at browser close
            else:
                request.session.set_expiry(1209600)  # 2 weeks

            return redirect('home')  # Change to your redirect URL
        else:
            return render(request, 'users/login.html', {'error': 'Invalid credentials'})
