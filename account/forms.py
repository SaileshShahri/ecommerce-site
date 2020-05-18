from django import forms
from django.conf import settings
from django.contrib.auth import forms as django_forms, update_session_auth_hash
from django.utils.translation import pgettext, pgettext_lazy


# from django.core.mail import send_mail
from .models import User


class LoginForm(django_forms.AuthenticationForm):
    username = forms.EmailField(label=pgettext("Form field", "Email"))

    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request=request, *args, **kwargs)
        if request:
            email = request.GET.get("email")
            if email:
                self.fields["username"].initial = email


class SignupForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput, label=pgettext("Password", "Password")
    )
    email = forms.EmailField(
        label=pgettext("Email", "Email"),
        error_messages={
            "unique": pgettext_lazy(
                "Registration error", "This email has already been registered."
            )
        },
    )

    class Meta:
        model = User
        fields = (
                "email",
                "name",
                "phonenumber",
                "password",
            )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self._meta.model.USERNAME_FIELD in self.fields:
            self.fields[self._meta.model.USERNAME_FIELD].widget.attrs.update(
                {"autofocus": ""}
            )

    def save(self, request=None, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data["password"]
        user.set_password(password)
        if commit:
            user.save()
            # account_events.customer_account_created_event(user=user)
            # get_extensions_manager().customer_created(customer=user)
        return user



class PasswordResetForm(django_forms.PasswordResetForm):
    """Allow resetting passwords.

    This subclass overrides sending emails to use templated email.
    """

    def get_users(self, email):
        active_users = User.objects.filter(email__iexact=email, active=True)
        return active_users

    def send_mail(
        self,
        subject_template_name,
        email_template_name,
        context,
        from_email,
        to_email,
        html_email_template_name=None,
    ):
        # Passing the user object to the Celery task throws an
        # error "'User' is not JSON serializable". Since it's not used in our
        # template, we remove it from the context.
        user = context.pop("user")
        # emails.send_user_password_reset_email(to_email, context, user.pk)

class UserForm(forms.ModelForm):
    """
    User-related CRUD form
    """
    class Meta:
        model = User
        fields = [
            'email',
            'name',
            'phonenumber',
            ]

