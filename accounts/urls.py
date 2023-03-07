from django.urls import path
from accounts.views import user_log_in, user_log_out, user_sign_up

urlpatterns = [
    path("login/", user_log_in, name="login"),
    path("logout/", user_log_out, name="logout"),
    path("signup/", user_sign_up, name="signup"),
]
