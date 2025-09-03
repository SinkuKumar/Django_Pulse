from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    # Project URLs
    path('', views.ProjectListView.as_view(), name='project_list'),
    path('create/', views.ProjectCreateView.as_view(), name='project_create'),
    path('<int:pk>/', views.ProjectDetailView.as_view(), name='project_detail'),
    path('<int:pk>/update/', views.ProjectUpdateView.as_view(), name='project_update'),

    # Milestone URLs
    path('<int:project_id>/milestones/', views.MilestoneListView.as_view(), name='milestone_list'),
    path('<int:project_id>/milestones/create/', views.MilestoneCreateView.as_view(), name='milestone_create'),
    path('<int:pk>/milestones/update/', views.MilestoneUpdateView.as_view(), name='milestone_update'),

    # AJAX endpoints for dynamic status options
    path('ajax/project-status/', views.ajax_project_status, name='ajax_project_status'),
    path('ajax/milestone-status/', views.ajax_milestone_status, name='ajax_milestone_status'),
]
