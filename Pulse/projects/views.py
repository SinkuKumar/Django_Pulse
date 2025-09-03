from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.http import JsonResponse
from django.urls import reverse_lazy
from .models import Project, Milestone, ProjectStatus, MilestoneStatus
from .forms import ProjectForm, MilestoneForm

# -----------------------
# Project Views
# -----------------------
class ProjectListView(ListView):
    model = Project
    template_name = 'projects/project_list.html'

    def get_queryset(self):
        # Show projects for logged-in user
        return Project.objects.filter(owner=self.request.user)


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/project_detail.html'

    def get_queryset(self):
        return Project.objects.filter(owner=self.request.user)


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/project_form.html'
    success_url = reverse_lazy('projects:project_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/project_form.html'
    success_url = reverse_lazy('projects:project_list')

    def get_queryset(self):
        return Project.objects.filter(owner=self.request.user)


# -----------------------
# Milestone Views
# -----------------------
class MilestoneListView(ListView):
    model = Milestone
    template_name = 'projects/milestone_list.html'

    def get_queryset(self):
        project_id = self.kwargs['project_id']
        project = get_object_or_404(Project, pk=project_id, owner=self.request.user)
        return Milestone.objects.filter(project=project)


class MilestoneCreateView(CreateView):
    model = Milestone
    form_class = MilestoneForm
    template_name = 'projects/milestone_form.html'

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs['project_id'], owner=self.request.user)
        form.instance.project = project
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('projects:milestone_list', kwargs={'project_id': self.kwargs['project_id']})


class MilestoneUpdateView(UpdateView):
    model = Milestone
    form_class = MilestoneForm
    template_name = 'projects/milestone_form.html'

    def get_queryset(self):
        return Milestone.objects.filter(project__owner=self.request.user)

    def get_success_url(self):
        return reverse_lazy('projects:milestone_list', kwargs={'project_id': self.object.project.id})


# -----------------------
# AJAX Views for dynamic choices
# -----------------------
def ajax_project_status(request):
    statuses = ProjectStatus.objects.filter(owner=request.user)
    data = [{'id': s.id, 'name': s.name} for s in statuses]
    return JsonResponse(data, safe=False)


def ajax_milestone_status(request):
    statuses = MilestoneStatus.objects.filter(owner=request.user)
    data = [{'id': s.id, 'name': s.name} for s in statuses]
    return JsonResponse(data, safe=False)
