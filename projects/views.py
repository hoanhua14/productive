from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from projects.models import Project


@login_required
def project_list(request):
    projects = Project.objects.filter(owner=request.user)
    context = {
        "projects": projects,
    }
    return render(request, "projects/list.html", context)
