from django.shortcuts import render, redirect
from tasks.models import Task
from tasks.forms import CreateTask
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def create_task(request):
    if request.method == "POST":
        form = CreateTask(request.POST)
        if form.is_valid:
            task = form.save()

            return redirect("list_projects")
    else:
        form = CreateTask()
    context = {"form": form}
    return render(request, "tasks/create.html", context)
