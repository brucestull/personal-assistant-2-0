from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

from base.mixins import RegistrationAcceptedMixin
from accounts.forms import CustomUserChangeForm, CustomUserCreationForm
from accounts.models import CustomUser
from config.settings.base import THE_SITE_NAME


class ForbiddenView(TemplateView):
    """
    View for the 403 Forbidden page.
    """

    template_name = "403.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Forbidden"
        context["the_site_name"] = THE_SITE_NAME
        return context


class CustomUserSignUpView(CreateView):
    """
    View for user to create a new account.
    """

    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

    def get_context_data(self, **kwargs):
        """
        Get the parent `context` and add `the_site_name` to the it.
        """
        context = super().get_context_data(**kwargs)
        context["the_site_name"] = THE_SITE_NAME
        return context


class CustomLoginView(LoginView):
    """
    Override the default login view. This will allow us to add the site
    name to the context and then display it on the page.
    """

    def get_context_data(self, **kwargs):
        """
        Get the parent `context` and add `the_site_name` to the it.
        """
        context = super().get_context_data(**kwargs)
        context["the_site_name"] = THE_SITE_NAME
        return context


class CustomUserUpdateView(
    RegistrationAcceptedMixin,
    UserPassesTestMixin,
    UpdateView,
):
    """
    View for user to update an existing account.
    """

    model = CustomUser
    form_class = CustomUserChangeForm
    success_url = reverse_lazy("login")
    template_name = "registration/update.html"

    def test_func(self):
        """
        Allow the user to edit only their own account.

        The `self.request.user` is the user that is currently logged
        in. The `self.get_object()` is the user (object) that is being
        updated (`UpdateView`).
        """
        return self.request.user == self.get_object()

    def get_context_data(self, **kwargs):
        """
        Get the parent `context` and add `the_site_name` to the it.
        """
        # Call the base implementation first to get a context:
        # In other words, get the existing context that Django is going
        # to already use and then add our new dictionary item to the
        # `context` dictionary.
        context = super().get_context_data(**kwargs)
        context["the_site_name"] = THE_SITE_NAME
        return context


class CustomUserDetailView(
    RegistrationAcceptedMixin,
    UserPassesTestMixin,
    DetailView,
):
    """
    View for user to view their account details.

    We are only specifying the `model` here because we are using the
    default template name that is created by Django.
    """

    model = CustomUser

    def test_func(self):
        """
        Only allow the user to view their own account details.
        """
        return self.request.user == self.get_object()

    def get_context_data(self, **kwargs):
        """
        Get the parent `context` and add `the_site_name` and/or
        `page_title` to the it.
        """
        context = super().get_context_data(**kwargs)
        context["the_site_name"] = THE_SITE_NAME
        context["page_title"] = (f"{self.object.username}'s User Information",)
        return context
