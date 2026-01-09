from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.email_signup, name="email_signup"),
    path("verify-email/<uuid:token>/", views.verify_email, name="verify_email"),
    path("set-password/", views.set_password, name="set_password"),
    path("personal-details/", views.personal_details, name="personal_details"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("resend-verification/", views.resend_verification, name="resend_verification"),
]
