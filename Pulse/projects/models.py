from django.db import models
from django.contrib.auth.models import User

class ProjectStatus(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='project_statuses')
    name = models.CharField(max_length=50)

    class Meta:
        unique_together = ('owner', 'name')

    def __str__(self):
        return self.name


class MilestoneStatus(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='milestone_statuses')
    name = models.CharField(max_length=50)

    class Meta:
        unique_together = ('owner', 'name')

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='owned_projects')
    members = models.ManyToManyField(User, related_name='projects')
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    status = models.ForeignKey(ProjectStatus, on_delete=models.SET_NULL, null=True, blank=True, related_name='projects')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Milestone(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='milestones')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    responsible = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='milestones')
    due_date = models.DateField()
    status = models.ForeignKey(MilestoneStatus, on_delete=models.SET_NULL, null=True, blank=True, related_name='milestones')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.project.name})"
