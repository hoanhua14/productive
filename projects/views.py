from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from projects.models import Project
from projects.forms import CreateForm

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


@login_required
def create_project(request):
    if request.method == "POST":
        form = CreateForm(request.POST)
        if form.is_valid:
            project = form.save(False)
            project.owner = request.user
            project.save()
            return redirect("list_projects")
    else:
        form = CreateForm()
    context = {"form": form}
    return render(request, "projects/create.html", context)
