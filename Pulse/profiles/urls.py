from django.urls import path
from profiles import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path("change-password/", views.change_password_ajax, name="change_password_ajax"),
]
