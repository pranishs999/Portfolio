from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "main"

urlpatterns = [
    path("", views.home, name="home"),
    path("contact/", views.contact_submit, name="contact_submit"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("logout/", views.logout_view, name="logout_view"),
    path("accounts/login/", auth_views.LoginView.as_view(), name="login"),
]
