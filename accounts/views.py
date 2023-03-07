from django.shortcuts import render, redirect
from accounts.forms import LogInForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def user_log_in(request):
    if request.method == "POST":
        form = LogInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("list_projects")
    else:
        form = LogInForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/login.html", context)


def user_log_out(request):
    logout(request)
    return redirect("login")
