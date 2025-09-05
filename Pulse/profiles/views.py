from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

from .forms import UserForm, ProfileForm

@login_required
def profile(request):
    if request.method == "POST":
        if "user_form" in request.POST:  # User form submit
            user_form = UserForm(request.POST, instance=request.user)
            if user_form.is_valid():
                user_form.save()
                messages.success(request, "User details updated successfully.")
                return redirect("profile")

        elif "profile_form" in request.POST:  # Profile form submit
            profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
            if profile_form.is_valid():
                profile_form.save()
                messages.success(request, "Profile updated successfully.")
                return redirect("profile")

    user_form = UserForm(instance=request.user)
    profile_form = ProfileForm(instance=request.user.profile)

    return render(request, "profiles/profile.html", {
        "user_form": user_form,
        "profile_form": profile_form,
        "password_form": PasswordChangeForm(user=request.user),  # pass to template
    })


@login_required
def change_password_ajax(request):
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # prevent logout
            return JsonResponse({"success": True, "message": "Password changed successfully."})
        else:
            return JsonResponse({"success": False, "errors": form.errors})
    return JsonResponse({"success": False, "message": "Invalid request."})
