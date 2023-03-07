from django.urls import path
from accounts.views import user_log_in

urlpatterns = [
    path("login/", user_log_in, name="login"),
]
