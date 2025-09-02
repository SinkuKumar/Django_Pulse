from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def app(request):
    return render(request, 'app/app.html')
