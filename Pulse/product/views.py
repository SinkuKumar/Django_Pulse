from django.shortcuts import render, redirect

def product(request):
    # If user is authenticated, redirect to app page
    if request.user.is_authenticated:
        return redirect('app')  # Use your app's URL name here
    
    return render(request, 'product/index.html')