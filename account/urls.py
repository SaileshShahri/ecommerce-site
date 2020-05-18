from django.urls import path, re_path
from django.contrib.auth import views as django_views

from . import views
from .views import (
        ProfileView,
        ProfileUpdateView,
        login,
        logout,
        password_reset,
    )

urlpatterns = [
    # account create
    path("signup/", views.signup, name="signup"),
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),

    # profile edit 
    path("", ProfileView.as_view(), name='accountprofile'),

    # profile edit 
    path("edit/", ProfileUpdateView.as_view(), name='profile-update'),

    # password reset 
    path("password/reset/", password_reset, name="resetpassword"),
    path("password/reset/done/", django_views.PasswordResetDoneView.as_view(template_name="account/password_reset_done.html"), name="reset-password-done"),
    re_path(r"^password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$", django_views.PasswordResetConfirmView.as_view(), name="reset-password-confirm"),
    path("password/reset/complete/", django_views.PasswordResetCompleteView.as_view(template_name="account/password_reset_from_key_done.html"), name="reset-password-complete"),

    # password change
    path('password/change/', django_views.PasswordChangeView.as_view(template_name='account/password_change.html'), name='password_change'),
    path('password/change/done/', django_views.PasswordChangeDoneView.as_view(template_name="account/password_change_done.html"), name='password_change_done'),

]
