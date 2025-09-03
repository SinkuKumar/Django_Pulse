from django import forms
from .models import Project, Milestone, ProjectStatus, MilestoneStatus


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'name',
            'description',
            'members',
            'start_date',
            'end_date',
            'status',
        ]
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }


class MilestoneForm(forms.ModelForm):
    class Meta:
        model = Milestone
        fields = [
            'title',
            'description',
            'responsible',
            'due_date',
            'status',
        ]
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }


class ProjectStatusForm(forms.ModelForm):
    class Meta:
        model = ProjectStatus
        fields = ['name']


class MilestoneStatusForm(forms.ModelForm):
    class Meta:
        model = MilestoneStatus
        fields = ['name']
