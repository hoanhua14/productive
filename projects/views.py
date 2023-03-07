from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from projects.models import Project

# from tasks.models import Task


@login_required
def project_list(request):
    projects = Project.objects.filter(owner=request.user)
    context = {
        "projects": projects,
    }
    return render(request, "projects/list.html", context)


@login_required
def show_project(request, id):
    projects = Project.objects.get(id=id)
    context = {
        "projects": projects,
    }
    return render(request, "projects/details.html", context)
